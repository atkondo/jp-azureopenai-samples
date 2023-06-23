# coding: utf-8

"""
    Speech to Text API v3.0

    Speech to Text API v3.0.  # noqa: E501

    OpenAPI spec version: v3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class Model(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'project': 'EntityReference',
        'links': 'ModelLinks',
        'properties': 'ModelProperties',
        '_self': 'str',
        'display_name': 'str',
        'description': 'str',
        'text': 'str',
        'base_model': 'EntityReference',
        'datasets': 'list[EntityReference]',
        'locale': 'str',
        'last_action_date_time': 'datetime',
        'status': 'str',
        'created_date_time': 'datetime',
        'custom_properties': 'dict(str, str)'
    }

    attribute_map = {
        'project': 'project',
        'links': 'links',
        'properties': 'properties',
        '_self': 'self',
        'display_name': 'displayName',
        'description': 'description',
        'text': 'text',
        'base_model': 'baseModel',
        'datasets': 'datasets',
        'locale': 'locale',
        'last_action_date_time': 'lastActionDateTime',
        'status': 'status',
        'created_date_time': 'createdDateTime',
        'custom_properties': 'customProperties'
    }

    def __init__(self, project=None, links=None, properties=None, _self=None, display_name=None, description=None, text=None, base_model=None, datasets=None, locale=None, last_action_date_time=None, status=None, created_date_time=None, custom_properties=None, _configuration=None):  # noqa: E501
        """Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._project = None
        self._links = None
        self._properties = None
        self.__self = None
        self._display_name = None
        self._description = None
        self._text = None
        self._base_model = None
        self._datasets = None
        self._locale = None
        self._last_action_date_time = None
        self._status = None
        self._created_date_time = None
        self._custom_properties = None
        self.discriminator = None

        if project is not None:
            self.project = project
        if links is not None:
            self.links = links
        if properties is not None:
            self.properties = properties
        if _self is not None:
            self._self = _self
        self.display_name = display_name
        if description is not None:
            self.description = description
        if text is not None:
            self.text = text
        if base_model is not None:
            self.base_model = base_model
        if datasets is not None:
            self.datasets = datasets
        self.locale = locale
        if last_action_date_time is not None:
            self.last_action_date_time = last_action_date_time
        if status is not None:
            self.status = status
        if created_date_time is not None:
            self.created_date_time = created_date_time
        if custom_properties is not None:
            self.custom_properties = custom_properties

    @property
    def project(self):
        """Gets the project of this Model.  # noqa: E501

        The project, the model is associated with.  # noqa: E501

        :return: The project of this Model.  # noqa: E501
        :rtype: EntityReference
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this Model.

        The project, the model is associated with.  # noqa: E501

        :param project: The project of this Model.  # noqa: E501
        :type: EntityReference
        """

        self._project = project

    @property
    def links(self):
        """Gets the links of this Model.  # noqa: E501

        The links for additional actions or content related to this model.  # noqa: E501

        :return: The links of this Model.  # noqa: E501
        :rtype: ModelLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Model.

        The links for additional actions or content related to this model.  # noqa: E501

        :param links: The links of this Model.  # noqa: E501
        :type: ModelLinks
        """

        self._links = links

    @property
    def properties(self):
        """Gets the properties of this Model.  # noqa: E501

        Additional configuration options when creating a new model and additional metadata provided by the service.  # noqa: E501

        :return: The properties of this Model.  # noqa: E501
        :rtype: ModelProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Model.

        Additional configuration options when creating a new model and additional metadata provided by the service.  # noqa: E501

        :param properties: The properties of this Model.  # noqa: E501
        :type: ModelProperties
        """

        self._properties = properties

    @property
    def _self(self):
        """Gets the _self of this Model.  # noqa: E501

        The location of this entity.  # noqa: E501

        :return: The _self of this Model.  # noqa: E501
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this Model.

        The location of this entity.  # noqa: E501

        :param _self: The _self of this Model.  # noqa: E501
        :type: str
        """

        self.__self = _self

    @property
    def display_name(self):
        """Gets the display_name of this Model.  # noqa: E501

        The display name of the object.  # noqa: E501

        :return: The display_name of this Model.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Model.

        The display name of the object.  # noqa: E501

        :param display_name: The display_name of this Model.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this Model.  # noqa: E501

        The description of the object.  # noqa: E501

        :return: The description of this Model.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Model.

        The description of the object.  # noqa: E501

        :param description: The description of this Model.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def text(self):
        """Gets the text of this Model.  # noqa: E501

        The text used to adapt this language model.  # noqa: E501

        :return: The text of this Model.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Model.

        The text used to adapt this language model.  # noqa: E501

        :param text: The text of this Model.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def base_model(self):
        """Gets the base_model of this Model.  # noqa: E501

        The base model used for adaptation.  # noqa: E501

        :return: The base_model of this Model.  # noqa: E501
        :rtype: EntityReference
        """
        return self._base_model

    @base_model.setter
    def base_model(self, base_model):
        """Sets the base_model of this Model.

        The base model used for adaptation.  # noqa: E501

        :param base_model: The base_model of this Model.  # noqa: E501
        :type: EntityReference
        """

        self._base_model = base_model

    @property
    def datasets(self):
        """Gets the datasets of this Model.  # noqa: E501

        Datasets used for adaptation.  # noqa: E501

        :return: The datasets of this Model.  # noqa: E501
        :rtype: list[EntityReference]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        """Sets the datasets of this Model.

        Datasets used for adaptation.  # noqa: E501

        :param datasets: The datasets of this Model.  # noqa: E501
        :type: list[EntityReference]
        """

        self._datasets = datasets

    @property
    def locale(self):
        """Gets the locale of this Model.  # noqa: E501

        The locale of the contained data.  # noqa: E501

        :return: The locale of this Model.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this Model.

        The locale of the contained data.  # noqa: E501

        :param locale: The locale of this Model.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and locale is None:
            raise ValueError("Invalid value for `locale`, must not be `None`")  # noqa: E501

        self._locale = locale

    @property
    def last_action_date_time(self):
        """Gets the last_action_date_time of this Model.  # noqa: E501

        The time-stamp when the current status was entered.  The time stamp is encoded as ISO 8601 date and time format  (\"YYYY-MM-DDThh:mm:ssZ\", see https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations).  # noqa: E501

        :return: The last_action_date_time of this Model.  # noqa: E501
        :rtype: datetime
        """
        return self._last_action_date_time

    @last_action_date_time.setter
    def last_action_date_time(self, last_action_date_time):
        """Sets the last_action_date_time of this Model.

        The time-stamp when the current status was entered.  The time stamp is encoded as ISO 8601 date and time format  (\"YYYY-MM-DDThh:mm:ssZ\", see https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations).  # noqa: E501

        :param last_action_date_time: The last_action_date_time of this Model.  # noqa: E501
        :type: datetime
        """

        self._last_action_date_time = last_action_date_time

    @property
    def status(self):
        """Gets the status of this Model.  # noqa: E501

        The status of the object.  # noqa: E501

        :return: The status of this Model.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Model.

        The status of the object.  # noqa: E501

        :param status: The status of this Model.  # noqa: E501
        :type: str
        """
        allowed_values = ["NotStarted", "Running", "Succeeded", "Failed"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def created_date_time(self):
        """Gets the created_date_time of this Model.  # noqa: E501

        The time-stamp when the object was created.  The time stamp is encoded as ISO 8601 date and time format  (\"YYYY-MM-DDThh:mm:ssZ\", see https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations).  # noqa: E501

        :return: The created_date_time of this Model.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date_time

    @created_date_time.setter
    def created_date_time(self, created_date_time):
        """Sets the created_date_time of this Model.

        The time-stamp when the object was created.  The time stamp is encoded as ISO 8601 date and time format  (\"YYYY-MM-DDThh:mm:ssZ\", see https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations).  # noqa: E501

        :param created_date_time: The created_date_time of this Model.  # noqa: E501
        :type: datetime
        """

        self._created_date_time = created_date_time

    @property
    def custom_properties(self):
        """Gets the custom_properties of this Model.  # noqa: E501

        The custom properties of this entity. The maximum allowed key length is 64 characters, the maximum  allowed value length is 256 characters and the count of allowed entries is 10.  # noqa: E501

        :return: The custom_properties of this Model.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """Sets the custom_properties of this Model.

        The custom properties of this entity. The maximum allowed key length is 64 characters, the maximum  allowed value length is 256 characters and the count of allowed entries is 10.  # noqa: E501

        :param custom_properties: The custom_properties of this Model.  # noqa: E501
        :type: dict(str, str)
        """

        self._custom_properties = custom_properties

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Model, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Model):
            return True

        return self.to_dict() != other.to_dict()
