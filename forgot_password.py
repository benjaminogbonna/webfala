def forgot_password(email):
    print(f"Password reset link sent to {email}. Please check your inbox.")

def reset_password(token, new_password):
    print(f"Password has been reset using token: {token}. Your")

print("new password is now set. Please log in with your new password.")