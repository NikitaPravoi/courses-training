from django.core.mail import send_mail


def send_course_notification(course, recipient_email):
    subject = f'Notification: Course "{course.name}" starting tomorrow!'
    message = f'Dear student,\n\nReminding you, that "{course.name}" starts tomorrow. Please, be ready and sure, that you are ready to start study.\n\nBest regards, your course team.'
    from_email = 'admin@example.com'  # Replace with your email
    recipient_list = [recipient_email]

    send_mail(subject, message, from_email, recipient_list)
