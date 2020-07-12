#!/bin/bash

# Stop service
launchctl stop /Library/LaunchDaemons/dev.deimos.HeadHunterWebScraper
launchctl unload /Library/LaunchDaemons/dev.deimos.HeadHunterWebScraper.plist

# Load new version
sudo cp dev.deimos.HeadHunterWebScraper.plist /Library/LaunchDaemons/
launchctl load /Library/LaunchDaemons/dev.deimos.HeadHunterWebScraper.plist
launchctl start /Library/LaunchDaemons/dev.deimos.HeadHunterWebScraper

# Final check
launchctl list | grep dev.deimos.HeadHunterWebScraper