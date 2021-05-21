import datetime
import decimal
import json
import logging
import uuid

from .soap import settings

logger = logging.getLogger('pyfva')


def _get_duration_components(duration):
    days = duration.days
    seconds = duration.seconds
    microseconds = duration.microseconds

    minutes = seconds // 60
    seconds = seconds % 60

    hours = minutes // 60
    minutes = minutes % 60

    return days, hours, minutes, seconds, microseconds


def duration_iso_string(duration):
    if duration < datetime.timedelta(0):
        sign = '-'
        duration *= -1
    else:
        sign = ''

    days, hours, minutes, seconds, microseconds = _get_duration_components(duration)
    ms = '.{:06d}'.format(microseconds) if microseconds else ""
    return '{}P{}DT{:02d}H{:02d}M{:02d}{}S'.format(sign, days, hours, minutes, seconds, ms)


class DateTimeJSONEncoder(json.JSONEncoder):
    """
    JSONEncoder subclass that knows how to encode date/time, decimal types, and
    UUIDs.
    """

    def default(self, o):
        # See "Date Time String Format" in the ECMA-262 specification.
        if isinstance(o, datetime.datetime):
            r = o.isoformat()
            if o.microsecond:
                r = r[:23] + r[26:]
            if r.endswith('+00:00'):
                r = r[:-6] + 'Z'
            return r
        elif isinstance(o, datetime.date):
            return o.isoformat()
        elif isinstance(o, datetime.time):
            if o.utcoffset() is not None:
                raise ValueError("JSON can't represent timezone-aware times.")
            r = o.isoformat()
            if o.microsecond:
                r = r[:12]
            return r
        elif isinstance(o, datetime.timedelta):
            return duration_iso_string(o)
        elif isinstance(o, (decimal.Decimal, uuid.UUID)):
            return str(o)
        elif isinstance(o, Exception):
            return str(o)
        else:
            return super().default(o)


def convert_data(data):
    if not settings.LOGGING_PREFIX:
        return data
    datadev = {}
    for x, y in data.items():
        datadev[settings.LOGGING_PREFIX + str(x)] = y
    return datadev


def info(data):
    data['sector'] = 'pyfva'
    logger.info(
        json.dumps(convert_data(data), cls=DateTimeJSONEncoder)
    )


def warning(data):
    data['sector'] = 'pyfva'
    logger.warning(
        json.dumps(convert_data(data), cls=DateTimeJSONEncoder)
    )


def debug(data):
    data['sector'] = 'pyfva'
    logger.debug(
        json.dumps(convert_data(data), cls=DateTimeJSONEncoder)
    )


def error(data):
    data['sector'] = 'pyfva'
    logger.error(
        json.dumps(convert_data(data), cls=DateTimeJSONEncoder)
    )
