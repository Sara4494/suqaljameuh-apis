from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from users.permissions import UserActive
from varieties.models import Currency, City, Country
from memberships.models import AdMembership, UserMembership
from globals.payment_helpers import create_charge, create_customer
from globals.global_tasks import reward_user
from globals.ad_helpers import update_ad_type
from jobs.models import JobOffer, ExperienceLevel, ContractType, Grade
from users.permissions import UserOwnerOnly


@api_view(["POST"])
@permission_classes([UserActive, UserOwnerOnly])
def publish_ad(request, ad_id):
    data = request.data

    if not data or data == None:
        return Response({
            "message": "Nothing To Update"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        ad = JobOffer.objects.get(pk=ad_id)
    except JobOffer.DoesNotExist:
        return Response({
            "message": "couldn't find this offer"
        }, status=status.HTTP_404_NOT_FOUND)

    # * These data are mandatory, and mostly doesn't change over the time
    job_title = data.get("title")
    job_description = data.get("description")
    country = data.get("country")
    city = data.get("city")
    currency = data.get("currency")
    salary = data.get("salary")
    phone_number = data.get("phone_number")
    contract_type = data.get("contract_type")
    working_days = data.get("working_days")
    work_from_home = data.get("work_from_home")
    require_license = data.get("require_license")
    require_vehicle = data.get("require_vehicle")
    shift_system = data.get("shift_system")
    grade = data.get("grade")
    exp_level = data.get("exp_level")
    gender = data.get("gender")

    try:
        is_updated = False
        if job_title and ad.job_title != job_title:
            ad.job_title = job_title
            is_updated = True

        if job_description and ad.job_description != job_description:
            ad.job_description = job_description
            is_updated = True

        if salary and ad.salary != salary:
            ad.salary = salary
            is_updated = True

        if phone_number and ad.phone_number != phone_number:
            ad.phone_number = phone_number
            is_updated = True

        if working_days and ad.working_days != working_days:
            ad.working_days = working_days
            is_updated = True

        if work_from_home and ad.work_from_home != work_from_home:
            ad.work_from_home = work_from_home
            is_updated = True

        if require_license and ad.require_license != require_license:
            ad.require_license = require_license
            is_updated = True

        if require_vehicle and ad.require_vehicle != require_vehicle:
            ad.require_vehicle = require_vehicle
            is_updated = True

        if shift_system and ad.shift_system != shift_system:
            ad.shift_system = shift_system
            is_updated = True

        if gender and ad.gender != gender:
            ad.gender = gender
            is_updated = True

        if contract_type and ad.contract_type.name != contract_type:
            try:
                contract_type_model = ContractType.objects.get(
                    name=contract_type)
            except ContractType.DoesNotExist:
                return Response({
                    "message": "Cannot find contract type with this name"
                }, status=status.HTTP_404_NOT_FOUND)
            ad.contract_type = contract_type_model
            is_updated = True

        if country and ad.country.name != country:
            try:
                country_model = Country.objects.get(name=country)
            except Country.DoesNotExist:
                return Response({
                    "message": "Cannot find country with this name"
                }, status=status.HTTP_404_NOT_FOUND)
            ad.country = country_model
            is_updated = True

        if city and ad.city.name != city:
            try:
                city_model = City.objects.get(name=city)
            except City.DoesNotExist:
                return Response({
                    "message": "Cannot find city with this name"
                }, status=status.HTTP_404_NOT_FOUND)
            ad.city = city_model
            is_updated = True

        if currency and ad.currency.name != currency:
            try:
                currency_model = Currency.objects.get(name=currency)
            except Currency.DoesNotExist:
                return Response({
                    "message": "Cannot find currency with this name"
                }, status=status.HTTP_404_NOT_FOUND)
            ad.currency = currency_model
            is_updated = True

        if grade and ad.grade.name != grade:
            try:
                grade_model = Grade.objects.get(name=grade)
            except Grade.DoesNotExist:
                return Response({
                    "message": "Cannot find grade with this name"
                }, status=status.HTTP_404_NOT_FOUND)
            ad.grade = grade_model
            is_updated = True

        if exp_level and ad.exp_level.name != exp_level:
            try:
                exp_level_model = ExperienceLevel.objects.get(name=exp_level)
            except ExperienceLevel.DoesNotExist:
                return Response({
                    "message": "Cannot find experience level with this name"
                }, status=status.HTTP_404_NOT_FOUND)
            ad.exp_level = exp_level_model
            is_updated = True

        if is_updated == True:
            ad.save()
            return Response({
                "message": "your offer updated successfully"
            }, status=status.HTTP_200_OK)
        return Response({
            "message": "your offer updated successfully"
        }, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({
            "message": "an error occurred while updating the ad"
        }, status=status.HTTP_400_BAD_REQUEST)
