from ninja import Router
from django.contrib.auth import get_user_model
from custom_user.schema import AccountIn
from custom_user.schema import SignIn
from custom_user.authorization import create_token_for_user

authorization_router = Router(tags=['authorization'])
User = get_user_model()


@authorization_router.post('Signup',auth=None)
def signup(request, account_in: AccountIn):
    if account_in.password1 != account_in.password2:
        return 400, {'detail': 'Passwords should look alike'}

    try:
        User.objects.get(phone=account_in.phone)
    except:
        new_user = User.objects.create_user(
            name=account_in.name,
            phone = account_in.phone,
            password=account_in.password1
        )

        token = create_token_for_user(new_user)

        return {
                'token': token,
                'account': {
                    'name':new_user.name,
                    'phone': new_user.phone,
                    'user_id':new_user.id
                    }
            }

    return 404, {'detail':'there was an error'}



@authorization_router.post('signin',auth=None)
def signin(request, signin_in: SignIn):
    try:
        user = User.objects.get(phone=signin_in.phone)
    except User.DoesNotExist:
        user = None

    else:
        if user.check_password(signin_in.password):
            token = create_token_for_user(user)
            return {
                'token': token,
                'UserAccount': {
                    'name':user.name,
                    'phone': user.phone,
                    'user_id': user.id
                    }
            }

    if not user:
        return 404, {'detail':'there was an error'}


