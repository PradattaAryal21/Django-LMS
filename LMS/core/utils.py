from functools import wraps
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)

def handle_error(func):
    """
    Decorator to catch exceptions and handle errors uniformly.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
            return JsonResponse(
                {"error": "An unexpected error occurred", "details": str(e)},
                status=500,
            )
    return wrapper
