#!/bin/bash

PROJECT_NAME=dev.deimos.HeadHunterWebScraper

PROJECT_ROOT=$PWD/..
PROJECT_CONFIG_DIR=$PROJECT_ROOT/config
PROJECT_BUILD_DIR=$PROJECT_ROOT/build
PROJECT_BINARY_DIR=$PROJECT_BUILD_DIR/dist
PROJECT_CONFIG_PATH=$PROJECT_CONFIG_DIR/config.json
PROJECT_BINARY_PATH=$PROJECT_BINARY_DIR/$PROJECT_NAME

MAIN_SCRIPT_PATH=$PROJECT_ROOT/src/main.py
PLIST_FILE_PATH=$PROJECT_ROOT/$PROJECT_NAME.plist

TARGET_INSTALL_DIR=/usr/local
TARGET_CONFIG_DIR=$TARGET_INSTALL_DIR/share/$PROJECT_NAME/config
TARGET_BINARY_DIR=$TARGET_INSTALL_DIR/bin
TARGET_CONFIG_PATH=$TARGET_CONFIG_DIR/config.json
TARGET_BINARY_PATH=$TARGET_BINARY_DIR/$PROJECT_NAME

function installDependency
{
    # Install pyinstaller for generatin binary
    sudo pip install pyinstaller
}

function build
{
    cd $PROJECT_BUILD_DIR
    sudo pyinstaller --onefile --noconsole $MAIN_SCRIPT_PATH --name $PROJECT_NAME
    cd $PROJECT_ROOT
}

function loadService
{
    plutil $PROJECT_NAME.plist

    # Stop service
    launchctl stop /Library/LaunchDaemons/$PROJECT_NAME
    launchctl unload /Library/LaunchDaemons/$PROJECT_NAME.plist

    # Load new version
    sudo cp $PLIST_FILE_PATH /Library/LaunchDaemons/
    launchctl load /Library/LaunchDaemons/$PROJECT_NAME.plist
    launchctl start /Library/LaunchDaemons/$PROJECT_NAME

    # Final check
    launchctl list | grep $PROJECT_NAME
}

function setupPlist
{
    plutil -remove ProgramArguments.0 $PLIST_FILE_PATH
    plutil -replace ProgramArguments.0 -string $TARGET_BINARY_PATH $PLIST_FILE_PATH

    plutil -remove EnvironmentVariables.HEAD_HUNTER_WEB_SCRAPER_CONFIG_PATH $PLIST_FILE_PATH
    plutil -replace EnvironmentVariables.HEAD_HUNTER_WEB_SCRAPER_CONFIG_PATH -string $TARGET_CONFIG_PATH $PLIST_FILE_PATH
}

function install
{
    sudo mkdir -p $TARGET_CONFIG_DIR
    sudo cp $PROJECT_CONFIG_PATH $TARGET_CONFIG_DIR
    sudo cp $PROJECT_BINARY_PATH $TARGET_BINARY_PATH
    sudo touch /var/log/$PROJECT_NAME.log
    sudo chown $USER /var/log/$PROJECT_NAME.log

    setupPlist
    loadService
}

function remove
{
    sudo rm -rf $TARGET_INSTALL_DIR/share/$PROJECT_NAME
    sudo rm -f $TARGET_BINARY_PATH
    sudo rm -f /var/log/$PROJECT_NAME.log
}

remove
installDependency
build
install

