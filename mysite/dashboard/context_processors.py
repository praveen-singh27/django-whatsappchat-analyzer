from analysis.models import Customer

def customer_context(request):
    customer = None
    if 'customer_id' in request.session:
        try:
            customer = Customer.objects.get(id=request.session['customer_id'])
        except Customer.DoesNotExist:
            request.session.flush()  # Clear session if customer doesn't exist
    return {'customer': customer}


def selected_user_processor(request):
    """ Make selected user available globally in templates """
    selected_user = request.session.get('selected_user', None)
    return {'selected_user': selected_user}

