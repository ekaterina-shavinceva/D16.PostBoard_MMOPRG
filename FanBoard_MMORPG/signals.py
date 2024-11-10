# from django.contrib.auth.models import User
# from django.db.models.signals import post_save, pre_save
# from django.dispatch import receiver
# from django.core.mail import send_mail, EmailMultiAlternatives
# from .models import UserResponse, Category
#
#
# # @receiver(post_save, sender=UserResponse)
# # def my_handler(sender, instance, created, **kwargs):
# #     if not instance.status == True:
# #         return
# #     mail = instance.article.author.email
# #     send_mail(
# #         'заголовок',
# #         'текст',
# #         'host@mail.ru',
# #         [mail],
# #         fail_silently=False,
# #     )
#
# @receiver(post_save, sender=Category)
# def product_created(instance, created, **kwargs):
#     if not created:
#         return
#
#     emails = User.objects.filter(
#         subscriptions__category=instance.category
#     ).values_list('email', flat=True)
#
#     subject = f'Новое объявление {instance.category}'
#
#     text_content = (
#         f'Заголовок: {instance.title}\n'
#         f'Текст: {instance.text}\n\n'
#         f'Ссылка на товар: http://127.0.0.1:8000{instance.get_absolute_url()}'
#     )
#     html_content = (
#         f'Заголовок: {instance.title}<br>'
#         f'Текст: {instance.text}<br><br>'
#         f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
#         f'Ссылка на товар</a>'
#     )
#     for email in emails:
#         msg = EmailMultiAlternatives(subject, text_content, None, [email])
#         msg.attach_alternative(html_content, "text/html")
#         msg.send()