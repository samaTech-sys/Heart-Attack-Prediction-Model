import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
    __version__ = "0.0.0" #Version of the project
    
    REPO_NAME = "Heart-Attack-Prediction-Model" #Name of project Reopository at github
    AUTHOR_USER_NAME = "samaTech-sys"#Github username of the developer
    SRC_REPO = "heartAttack" #Folder with project files 
    AUTHOR_EMAIL = "collinetazuba@gmail.com" #Email of project developer 
    
    setuptools.setup(
        name=SRC_REPO, 
        version=__version__, 
        author=AUTHOR_USER_NAME, 
        author_email=AUTHOR_EMAIL, 
        description="This project trainns a logistic regression model for predicting heat attack based on available parameters. It will aid deoctors in descision making while at deployment stage", 
        long_description=long_description, 
        long_description_content_type="text/markdown", 
        url="https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}", 
        project_urls={
            "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
        }, 
        package_dir={"": "src"}, 
        packages= setuptools.find_packages(where="src")
    )