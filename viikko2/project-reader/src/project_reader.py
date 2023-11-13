from urllib import request
from project import Project
import tomlkit


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        data = tomlkit.loads(content)["tool"]["poetry"]
        license = data["license"]
        authors = [author for author in data["authors"]]
        dependencies = [dependency for dependency in data["dependencies"]]
        dev_dependencies = [
            dev_dependency for dev_dependency in data["group"]["dev"]["dependencies"]]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(data["name"], data["description"], license, authors, dependencies, dev_dependencies)
