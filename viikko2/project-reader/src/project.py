class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors if isinstance(authors, list) else [authors]
        self.dependencies = dependencies if isinstance(
            dependencies, list) else [dependencies]
        self.dev_dependencies = dev_dependencies if isinstance(
            dev_dependencies, list) else [dev_dependencies]

    def _stringify_dependencies_or_authors(self, data):
        return "\n- ".join(data) if len(data) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}\n"
            f"\nAuthors:\n- {self._stringify_dependencies_or_authors(self.authors)}\n"
            f"\nDependencies:\n- {self._stringify_dependencies_or_authors(self.dependencies)}\n"
            f"\nDevelopment dependencies:\n- {self._stringify_dependencies_or_authors(self.dev_dependencies)}"
        )
