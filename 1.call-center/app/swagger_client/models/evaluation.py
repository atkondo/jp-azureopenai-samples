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


class Evaluation(object):
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
        'model1': 'EntityReference',
        'model2': 'EntityReference',
        'transcription1': 'EntityReference',
        'transcription2': 'EntityReference',
        'dataset': 'EntityReference',
        'links': 'Links',
        'properties': 'EvaluationProperties',
        'project': 'EntityReference',
        '_self': 'str',
        'last_action_date_time': 'datetime',
        'status': 'str',
        'created_date_time': 'datetime',
        'display_name': 'str',
        'description': 'str',
        'custom_properties': 'dict(str, str)',
        'locale': 'str'
    }

    attribute_map = {
        'model1': 'model1',
        'model2': 'model2',
        'transcription1': 'transcription1',
        'transcription2': 'transcription2',
        'dataset': 'dataset',
        'links': 'links',
        'properties': 'properties',
        'project': 'project',
        '_self': 'self',
        'last_action_date_time': 'lastActionDateTime',
        'status': 'status',
        'created_date_time': 'createdDateTime',
        'display_name': 'displayName',
        'description': 'description',
        'custom_properties': 'customProperties',
        'locale': 'locale'
    }

    def __init__(self, model1=None, model2=None, transcription1=None, transcription2=None, dataset=None, links=None, properties=None, project=None, _self=None, last_action_date_time=None, status=None, created_date_time=None, display_name=None, description=None, custom_properties=None, locale=None, _configuration=None):  # noqa: E501
        """Evaluation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._model1 = None
        self._model2 = None
        self._transcription1 = None
        self._transcription2 = None
        self._dataset = None
        self._links = None
        self._properties = None
        self._project = None
        self.__self = None
        self._last_action_date_time = None
        self._status = None
        self._created_date_time = None
        self._display_name = None
        self._description = None
        self._custom_properties = None
        self._locale = None
        self.discriminator = None

        self.model1 = model1
        self.model2 = model2
        if transcription1 is not None:
            self.transcription1 = transcription1
        if transcription2 is not None:
            self.transcription2 = transcription2
        self.dataset = dataset
        if links is not None:
            self.links = links
        if properties is not None:
            self.properties = properties
        if project is not None:
            self.project = project
        if _self is not None:
            self._self = _self
        if last_action_date_time is not None:
            self.last_action_date_time = last_action_date_time
        if status is not None:
            self.status = status
        if created_date_time is not None:
            self.created_date_time = created_date_time
        self.display_name = display_name
        if description is not None:
            self.description = description
        if custom_properties is not None:
            self.custom_properties = custom_properties
        self.locale = locale

    @property
    def model1(self):
        """Gets the model1 of this Evaluation.  # noqa: E501

        The first model that can be used to evaluate the improvements and differences.  # noqa: E501

        :return: The model1 of this Evaluation.  # noqa: E501
        :rtype: EntityReference
        """
        return self._model1

    @model1.setter
    def model1(self, model1):
        """Sets the model1 of this Evaluation.

        The first model that can be used to evaluate the improvements and differences.  # noqa: E501

        :param model1: The model1 of this Evaluation.  # noqa: E501
        :type: EntityReference
        """
        if self._configuration.client_side_validation and model1 is None:
            raise ValueError("Invalid value for `model1`, must not be `None`")  # noqa: E501

        self._model1 = model1

    @property
    def model2(self):
        """Gets the model2 of this Evaluation.  # noqa: E501

        The second model that can be used to evaluate the improvements and differences.  # noqa: E501

        :return: The model2 of this Evaluation.  # noqa: E501
        :rtype: EntityReference
        """
        return self._model2

    @model2.setter
    def model2(self, model2):
        """Sets the model2 of this Evaluation.

        The second model that can be used to evaluate the improvements and differences.  # noqa: E501

        :param model2: The model2 of this Evaluation.  # noqa: E501
        :type: EntityReference
        """
        if self._configuration.client_side_validation and model2 is None:
            raise ValueError("Invalid value for `model2`, must not be `None`")  # noqa: E501

        self._model2 = model2

    @property
    def transcription1(self):
        """Gets the transcription1 of this Evaluation.  # noqa: E501

        Information about the transcriptions used in the evaluation with model1.  # noqa: E501

        :return: The transcription1 of this Evaluation.  # noqa: E501
        :rtype: EntityReference
        """
        return self._transcription1

    @transcription1.setter
    def transcription1(self, transcription1):
        """Sets the transcription1 of this Evaluation.

        Information about the transcriptions used in the evaluation with model1.  # noqa: E501

        :param transcription1: The transcription1 of this Evaluation.  # noqa: E501
        :type: EntityReference
        """

        self._transcription1 = transcription1

    @property
    def transcription2(self):
        """Gets the transcription2 of this Evaluation.  # noqa: E501

        Information about the transcriptions used in the evaluation with model2.  # noqa: E501

        :return: The transcription2 of this Evaluation.  # noqa: E501
        :rtype: EntityReference
        """
        return self._transcription2

    @transcription2.setter
    def transcription2(self, transcription2):
        """Sets the transcription2 of this Evaluation.

        Information about the transcriptions used in the evaluation with model2.  # noqa: E501

        :param transcription2: The transcription2 of this Evaluation.  # noqa: E501
        :type: EntityReference
        """

        self._transcription2 = transcription2

    @property
    def dataset(self):
        """Gets the dataset of this Evaluation.  # noqa: E501

        Information about the dataset used in the evaluation.  # noqa: E501

        :return: The dataset of this Evaluation.  # noqa: E501
        :rtype: EntityReference
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this Evaluation.

        Information about the dataset used in the evaluation.  # noqa: E501

        :param dataset: The dataset of this Evaluation.  # noqa: E501
        :type: EntityReference
        """
        if self._configuration.client_side_validation and dataset is None:
            raise ValueError("Invalid value for `dataset`, must not be `None`")  # noqa: E501

        self._dataset = dataset

    @property
    def links(self):
        """Gets the links of this Evaluation.  # noqa: E501

        The links for additional actions or content related to this evaluation.  # noqa: E501

        :return: The links of this Evaluation.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Evaluation.

        The links for additional actions or content related to this evaluation.  # noqa: E501

        :param links: The links of this Evaluation.  # noqa: E501
        :type: Links
        """

        self._links = links

    @property
    def properties(self):
        """Gets the properties of this Evaluation.  # noqa: E501

        Additional configuration options when creating a new evaluation and additional metadata provided by the service.  # noqa: E501

        :return: The properties of this Evaluation.  # noqa: E501
        :rtype: EvaluationProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Evaluation.

        Additional configuration options when creating a new evaluation and additional metadata provided by the service.  # noqa: E501

        :param properties: The properties of this Evaluation.  # noqa: E501
        :type: EvaluationProperties
        """

        self._properties = properties

    @property
    def project(self):
        """Gets the project of this Evaluation.  # noqa: E501

        The project, the evaluation is associated with.  # noqa: E501

        :return: The project of this Evaluation.  # noqa: E501
        :rtype: EntityReference
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this Evaluation.

        The project, the evaluation is associated with.  # noqa: E501

        :param project: The project of this Evaluation.  # noqa: E501
        :type: EntityReference
        """

        self._project = project

    @property
    def _self(self):
        """Gets the _self of this Evaluation.  # noqa: E501

        The location of this entity.  # noqa: E501

        :return: The _self of this Evaluation.  # noqa: E501
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this Evaluation.

        The location of this entity.  # noqa: E501

        :param _self: The _self of this Evaluation.  # noqa: E501
        :type: str
        """

        self.__self = _self

    @property
    def last_action_date_time(self):
        """Gets the last_action_date_time of this Evaluation.  # noqa: E501

        The time-stamp when the current status was entered.  The time stamp is encoded as ISO 8601 date and time format  (\"YYYY-MM-DDThh:mm:ssZ\", see https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations).  # noqa: E501

        :return: The last_action_date_time of this Evaluation.  # noqa: E501
        :rtype: datetime
        """
        return self._last_action_date_time

    @last_action_date_time.setter
    def last_action_date_time(self, last_action_date_time):
        """Sets the last_action_date_time of this Evaluation.

        The time-stamp when the current status was entered.  The time stamp is encoded as ISO 8601 date and time format  (\"YYYY-MM-DDThh:mm:ssZ\", see https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations).  # noqa: E501

        :param last_action_date_time: The last_action_date_time of this Evaluation.  # noqa: E501
        :type: datetime
        """

        self._last_action_date_time = last_action_date_time

    @property
    def status(self):
        """Gets the status of this Evaluation.  # noqa: E501

        The status of the object.  # noqa: E501

        :return: The status of this Evaluation.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Evaluation.

        The status of the object.  # noqa: E501

        :param status: The status of this Evaluation.  # noqa: E501
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
        """Gets the created_date_time of this Evaluation.  # noqa: E501

        The time-stamp when the object was created.  The time stamp is encoded as ISO 8601 date and time format  (\"YYYY-MM-DDThh:mm:ssZ\", see https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations).  # noqa: E501

        :return: The created_date_time of this Evaluation.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date_time

    @created_date_time.setter
    def created_date_time(self, created_date_time):
        """Sets the created_date_time of this Evaluation.

        The time-stamp when the object was created.  The time stamp is encoded as ISO 8601 date and time format  (\"YYYY-MM-DDThh:mm:ssZ\", see https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations).  # noqa: E501

        :param created_date_time: The created_date_time of this Evaluation.  # noqa: E501
        :type: datetime
        """

        self._created_date_time = created_date_time

    @property
    def display_name(self):
        """Gets the display_name of this Evaluation.  # noqa: E501

        The display name of the object.  # noqa: E501

        :return: The display_name of this Evaluation.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Evaluation.

        The display name of the object.  # noqa: E501

        :param display_name: The display_name of this Evaluation.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this Evaluation.  # noqa: E501

        The description of the object.  # noqa: E501

        :return: The description of this Evaluation.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Evaluation.

        The description of the object.  # noqa: E501

        :param description: The description of this Evaluation.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def custom_properties(self):
        """Gets the custom_properties of this Evaluation.  # noqa: E501

        The custom properties of this entity. The maximum allowed key length is 64 characters, the maximum  allowed value length is 256 characters and the count of allowed entries is 10.  # noqa: E501

        :return: The custom_properties of this Evaluation.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """Sets the custom_properties of this Evaluation.

        The custom properties of this entity. The maximum allowed key length is 64 characters, the maximum  allowed value length is 256 characters and the count of allowed entries is 10.  # noqa: E501

        :param custom_properties: The custom_properties of this Evaluation.  # noqa: E501
        :type: dict(str, str)
        """

        self._custom_properties = custom_properties

    @property
    def locale(self):
        """Gets the locale of this Evaluation.  # noqa: E501

        The locale of the contained data.  # noqa: E501

        :return: The locale of this Evaluation.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this Evaluation.

        The locale of the contained data.  # noqa: E501

        :param locale: The locale of this Evaluation.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and locale is None:
            raise ValueError("Invalid value for `locale`, must not be `None`")  # noqa: E501

        self._locale = locale

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
        if issubclass(Evaluation, dict):
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
        if not isinstance(other, Evaluation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Evaluation):
            return True

        return self.to_dict() != other.to_dict()