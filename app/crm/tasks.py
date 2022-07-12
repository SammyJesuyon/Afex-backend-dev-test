from __future__ import absolute_import, unicode_literals
from django.db import IntegrityError
import requests
from celery import shared_task
from .models import Client


@shared_task
def populate_clients():
    try:
        response = requests.get(
            'https://62c2c06cff594c656764970a.mockapi.io/users')
        if response.status_code != 200:
            raise Exception('API call failed')
        res = response.json()
        if res['message'] != 'success':
            raise Exception('API call failed')
        for items in res['data']:
            new_client = Client(
                cid=items['cid'],
                first_name=items['first_name'],
                last_name=items['last_name'],
                country_code=items['country_code'],
                email=items['email'],
                address=items['address'],
                phone=items['phone']
            )
            try:
                new_client.save()
            except IntegrityError:
                print('CID Exist')
                continue

    except:
        pass

    finally:
        return True

# @shared_task
# def add(x,y):
#     return x+y
