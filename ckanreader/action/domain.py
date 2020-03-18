from typing import Dict, Any, List
from urllib.request import urlretrieve
from urllib.parse import urlsplit
import os

from ckanreader.base import CkanRequest
from ckanreader.settings import AppConfig


class Tag:

    def __init__(self, result: Dict[str, Any]):
        self.vocabulary_id = result.get("vocabulary_id", "")
        self.display_name = result.get("display_name", "")
        self.id = result.get("id", "")
        self.name = result.get("name", "")

    @classmethod
    def list(cls, request: CkanRequest):
        response = request.gets("tag_list")
        results = response.pop("result")

        name_dict_list = [{"name": name} for name in results]

        tags = list()

        for result in name_dict_list:
            tag_instance = cls(result)
            tags.append(tag_instance)

        return tags

    @classmethod
    def show(cls, request: CkanRequest, id: str):
        query = {"id": id}
        response = request.gets("tag_show", query=query)

        result = response.pop("result")
        tag_instance = cls(result)

        return tag_instance


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


class User:

    def __init__(self, result: Dict[str, Any]):
        self.email_hash = result.get("email_hash", "")
        self.about = result.get("about", "")
        self.capacity = result.get("capacity", "")
        self.name = result.get("name", "")
        self.created = result.get("created", "")
        self.sysadmin = result.get("sysadmin", "")
        self.activity_streams_email_notifications = result.get(
            "activity_streams_email_notifications", "")
        self.state = result.get("state", "")
        self.number_of_edits = result.get("number_of_edits", "")
        self.display_name = result.get("display_name", "")
        self.fullname = result.get("fullname", "")
        self.id = result.get("id", "")
        self.number_created_packages = result.get(
            "number_created_packages", "")


class Group:

    def __init__(self, result: Dict[str, Any]):

        users = list()
        for user in result.get("users", []):
            user_instance = User(user)
            users.append(user_instance)
        self.users = users

        self.display_name = result.get("display_name", "")
        self.description = result.get("description", "")
        self.image_display_url = result.get("image_display_url", "")
        self.package_count = result.get("package_count", "")

        self.created = result.get("created", "")
        self.name = result.get("name", "")
        self.is_organization = result.get("is_organization", "")
        self.state = result.get("state", "")
        self.extras = result.get("extras", [])
        self.image_url = result.get("image_url", "")

        groups = list()
        for group in result.get("groups", []):
            group_instance = Group(group)
            groups.append(group_instance)
        self.groups = groups

        self.type = result.get("type", "")
        self.title = result.get("title", "")
        self.revision_id = result.get("revision_id", "")
        self.num_followers = result.get("num_followers", "")
        self.id = result.get("id", "")

        tags = list()
        for tag in result.get("tags", []):
            tag_instance = Tag(tag)
            tags.append(tag_instance)
        self.tags = tags

        self.approval_status = result.get("approval_status", "")

    @classmethod
    def list(cls, request: CkanRequest):
        response = request.gets("group_list")
        results = response.pop("result")

        name_dict_list = [{"name": name} for name in results]

        groups = list()

        for result in name_dict_list:
            group_instance = cls(result)
            groups.append(group_instance)

        return groups

    @classmethod
    def show(cls, request: CkanRequest, id: str):
        query = {"id": id}
        response = request.gets("group_show", query=query)

        result = response.pop("result")
        group_instance = cls(result)

        return group_instance


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

        tags = list()
        for tag in result.get("tags", []):
            tag_instance = Tag(tag)
            tags.append(tag_instance)
        self.tags = tags

        groups = list()
        for group in result.get("groups", []):
            group_instance = Group(group)
            groups.append(group_instance)
        self.groups = groups

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
    def search(cls, request: CkanRequest, name: str, value: str) -> List:
        search_value = "{}:{}".format(name, value)
        query = {"query": search_value}
        response = request.gets("resource_search", query=query)
        results = response.get("result").pop("results")

        resources = list()

        for result in results:
            resource_instance = cls(result)
            resources.append(resource_instance)

        return resources

    def fetch_data(self) -> str:
        if not os.path.exists(AppConfig.DOWNLOAD_PATH):
            os.mkdir(AppConfig.DOWNLOAD_PATH)

        url_item = urlsplit(self.url)
        # urlsplitの2番目の要素はpath
        path_item = url_item[2]
        # /で文字列を分割して、一番最後の値がファイル名になっている
        file_name = path_item.split("/")[-1]
        local_filepath = os.path.join(AppConfig.DOWNLOAD_PATH, file_name)

        if os.path.exists(local_filepath):
            os.remove(local_filepath)
        # ファイルダウンロード
        urlretrieve(self.url, local_filepath)

        return local_filepath


class PackagesActivity:

    def __init__(self, request: CkanRequest):
        self.request = request

    def list(self):
        response = self.request.gets("recently_changed_packages_activity_list")
        return response
