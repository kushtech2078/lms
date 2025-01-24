from .models import DeviceTracking
from django.utils.timezone import now
from .utils import get_client_ip  # Assuming the get_client_ip function is in utils.py


class TrackIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get client IP
        ip_address = get_client_ip(request)

        # For MAC address, you would have to get it from the client-side (e.g., mobile app, etc.)
        mac_address = request.META.get('HTTP_X_MAC_ADDRESS', None)  # Example header sent by the client

        # Save the information to the database
        DeviceTracking.objects.create(
            ip_address=ip_address,
            mac_address=mac_address,
            created_at=now()
        )

        response = self.get_response(request)
        return response