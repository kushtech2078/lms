def get_client_ip(request):
    """
    Function to extract the client's IP address from the request.
    This handles scenarios where the client is behind a proxy.
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # Get the first IP address in the list
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip