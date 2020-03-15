from typing import Dict, Any

from ckanreader.base import CkanRequest


class Group:

    def __init__(self, request: CkanRequest):
        self.request = request

    @classmethod
    def list(cls, request: CkanRequest):
        response = request.gets("group_list")
        return response

    @classmethod
    def show(cls, request: CkanRequest, id: str):
        query = {"id": id}
        response = request.gets("group_show", query=query)
        return response


class Package:

    def __init__(self, result: Dict[str, Any]):
        self.license_title = result.get("license_title", "")
        self.maintainer = result.get("maintainer", "")
        self.relationships_as_object = result.get(
            "relationships_as_object", [])
        self.private = result.get("private", False)
        self.maintainer_email = result.get("maintainer_email", "")
        self.num_tags = result.get("num_tags", "")
        self.id = result.get("id", "")
        self.metadata_created = result.get("metadata_created", "")
        self.metadata_modified = result.get("metadata_modified", "")
        self.author = result.get("author", "")
        self.author_email = result.get("author_email", "")
        self.state = result.get("state", "")
        self.version = result.get("version", "")
        self.creator_user_id = result.get("creator_user_id", "")
        self.type = result.get("type", "")
        self.num_resources = result.get("num_resources", "")
        self.tags = result.get("tags", [])
        self.groups = result.get("groups", [])
        self.creator_user_id = result.get("creator_user_id", "")
        self.relationships_as_subject = result.get(
            "relationships_as_subject", [])
        self.name = result.get("name", "")
        self.isopen = result.get("isopen", "")
        self.url = result.get("url", "")
        self.notes = result.get("notes", "")
        self.title = result.get("title", "")
        self.extras = result.get("extras", [])
        self.license_url = result.get("license_url", "")
        self.organization = Organization(result.get("organization", ""))
        self.revision_id = result.get("revision_id", "")

        resources = list()

        for resource in result["resources"]:
            resource_instance = Resource(resource)
            resources.append(resource_instance)

        self.resources = resources

    @classmethod
    def list(cls, request: CkanRequest):
        response = request.gets("package_list")
        results = response.pop("result")

        name_dict_list = [{"name": name} for name in results]

        packages = list()

        for result in name_dict_list:
            package_instance = cls(result)
            packages.append(package_instance)

        return packages

    @classmethod
    def show(cls, request: CkanRequest, id):
        query = {"id": id}
        response = request.gets("package_show", query=query)
        result = response.pop("result")
        package_instance = cls(result)

        return package_instance

    @classmethod
    def search(cls, request: CkanRequest, name: str):
        query = {"q": name}
        response = request.gets("package_search", query=query)
        results = response.get("result").pop("results")
        packages = list()

        for result in results:
            package_instance = cls(result)
            packages.append(package_instance)

        return packages


class Tag:

    def __init__(self, request: CkanRequest):
        self.request = request

    @classmethod
    def list(cls, request: CkanRequest):
        response = request.gets("tag_list")
        return response

    @classmethod
    def show(cls, request: CkanRequest, id: str):
        query = {"id": id}
        response = request.gets("tag_show", query=query)
        return response


class Resource:

    def __init__(self, result: Dict[str, Any]):
        self.mimetype = result["mimetype"]
        self.cache_url = result["cache_url"]
        self.state = result["state"]
        self.hash = result["hash"]
        self.description = result["description"]
        self.format = result["format"]
        self.url = result["url"]
        self.created = result["created"]
        self.cache_last_updated = result["cache_last_updated"]
        self.package_id = result["package_id"]
        self.mimetype_inner = result["mimetype_inner"]
        self.last_modified = result["last_modified"]
        self.position = result["position"]
        self.revision_id = result["revision_id"]
        self.size = result["size"]
        self.url_type = result["url_type"]
        self.id = result["id"]
        self.resource_type = result["resource_type"]
        self.name = result["name"]

    @classmethod
    def search(cls, request: CkanRequest, name: str, value: str):
        search_value = "{}:{}".format(name, value)
        query = {"query": search_value}
        response = request.gets("resource_search", query=query)
        results = response.get("result").pop("results")

        resources = list()

        for result in results:
            resource_instance = cls(result)
            resources.append(resource_instance)

        return resources

    def fetch_data(self):
        print("fetch_data")


class PackagesActivity:

    def __init__(self, request: CkanRequest):
        self.request = request

    def list(self):
        response = self.request.gets("recently_changed_packages_activity_list")
        return response


class Organization:

    def __init__(self, result: Dict[str, Any]):
        self.description = result.get("description", "")
        self.created = result.get("created", "")
        self.title = result.get("title", "")
        self.name = result.get("name", "")
        self.is_organization = result.get("is_organization", "")
        self.state = result.get("state", "")
        self.image_url = result.get("image_url", "")
        self.revision_id = result.get("revision_id", "")
        self.type = result.get("type", "")
        self.id = result.get("id", "")
        self.approval_status = result.get("approval_status", "")
