






@login_required(login_url="admin_login")
def payment(request, template="users/payment.html"):

    # add_user_obj = User.objects.create_user(
    #     username="1234567890",
    #     email="john@doe.com",
    #     password="Test105*",
    #     first_name="John",
    #     last_name="Doe"
    # )
    #
    # add_user_profile_obj = UserProfile.objects.create(
    #     user=add_user_obj,
    #     bio="Lorem ipsum",
    #     gender=Gender.male
    # )

    return render(request, template, {"users": User.objects.all()})