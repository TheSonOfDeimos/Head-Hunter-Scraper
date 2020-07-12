import json

class ConfigLoader(object) :
    m_config_path = "/Users/levkargalov/Documents/Projects/Programming/Python/Head-Hunter-Scraper/config/config.json"

    m_default_profile_folder = ""
    m_profiles = []

    m_xpath_rase_resume_button = ""
    m_resume_page_url = ""
    m_login_page_url = ""

    @classmethod
    def initConfig(cls) :
        file_str = open(cls.m_config_path, "r", encoding="UTF-8").read()
        data = json.loads(file_str)
        firefox = data['firefox']
        head_hunter_urls = data['head_hunter_urls']

        cls.m_default_profile_folder = firefox['profile_path']
        cls.m_profiles = firefox['profiles']

        cls.m_xpath_rase_resume_button = head_hunter_urls['update_button_xpath']
        cls.m_resume_page_url = head_hunter_urls['resume_page']
        cls.m_login_page_url = head_hunter_urls['login_page']
    
    @classmethod
    def getProfileFolderPath(cls) :
        cls.initConfig()
        return cls.m_default_profile_folder

    @classmethod
    def getResumeUrl(cls) :
        cls.initConfig()
        return cls.m_resume_page_url

    @classmethod
    def getLoginUrl(cls) :
        cls.initConfig()
        return cls.m_login_page_url
    
    @classmethod
    def getUpdateButtonXpath(cls) :
        cls.initConfig()
        return cls.m_xpath_rase_resume_button

    @classmethod
    def getProfilesList(cls) :
        cls.initConfig()
        return cls.m_profiles
