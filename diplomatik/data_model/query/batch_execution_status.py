from datetime import datetime
from enum import Enum

from pydantic import BaseModel

from diplomatik.exceptions.exceptions import DataModelException
from diplomatik.utils.time_utils import DEFAULT_DATETIME_FORMAT


class BatchExecutionStatusType(Enum):
    """
    The batch's execution status
    """
    success = 'success'
    failed = 'failed'
    in_progress = 'in_progress'
    cancelled = 'cancelled'

    @classmethod
    def get_by_value(cls, value):
        """
        Gets the batch status type based on its string value

        :param value: the value to match
        :return: the query result type
        """
        for status in BatchExecutionStatusType:
            if status.value == value:
                return status

        raise DataModelException(f"{value} is not a valid batch execution status")


class BatchExecutionStatus(BaseModel):
    """
    The data class representing the execution status of a batch of queries
    """
    batch_id: str
    """Unique user provided ID to track the batch"""

    status: BatchExecutionStatusType = None
    """Status of the batch execution"""

    message: str = ''
    """Any messages on the execution"""

    last_completed_query_id: str = ''
    """ID of the last query of the batch that was completed successfully"""

    is_cancel: bool = False
    """True of the cancel execution flag is set"""

    started_at: datetime = None
    """Time the execution started, in UTC"""

    completed_at: datetime = None
    """Time the execution completed, in UTC"""

    def to_cachable_dict(self) -> dict:
        """
        Converts the execution status into a dict that can be serialized and cached
        :return: the cacheable dict
        """
        return {
            "batch_id": self.batch_id,
            "status": self.status.value,
            "message": self.message,
            "last_completed_query_id": self.last_completed_query_id if self.last_completed_query_id else '',
            "is_cancel": str(self.is_cancel) if self.is_cancel else 'False',
            "started_at": self.started_at.strftime(DEFAULT_DATETIME_FORMAT) if self.started_at else '',
            "completed_at": self.completed_at.strftime(DEFAULT_DATETIME_FORMAT) if self.completed_at else ''
        }

    @staticmethod
    def from_cachable_dict(batch_execution_status: dict):
        """
        Converts the dict into the execution status object

        :param batch_execution_status: the dict to deserialize
        :return: the execution status object
        :rtype: BatchExecutionStatus
        """
        batch_id = batch_execution_status['batch_id']
        status = BatchExecutionStatusType.get_by_value(batch_execution_status['status'])
        message = batch_execution_status['message']
        last_completed_query_id = batch_execution_status['last_completed_query_id']
        is_cancel = batch_execution_status['is_cancel'].lower() == 'True'

        started_at = None
        if "started_at" in batch_execution_status and batch_execution_status['started_at']:
            started_at = datetime.strptime(batch_execution_status["started_at"], DEFAULT_DATETIME_FORMAT)

        completed_at = None
        if 'completed_at' in batch_execution_status and batch_execution_status['completed_at']:
            completed_at = datetime.strptime(batch_execution_status['completed_at'], DEFAULT_DATETIME_FORMAT)

        return BatchExecutionStatus(batch_id=batch_id,
                                    status=status,
                                    message=message,
                                    last_completed_query_id=last_completed_query_id,
                                    is_cancel=is_cancel,
                                    started_at=started_at,
                                    completed_at=completed_at)
