from django.shortcuts import render
from .models import *
import json 
from django.http import HttpResponse, JsonResponse
from django.middleware.csrf import get_token

# Create your views here.




#User ----------------------





# Merchant ---------------------------
def registerMerchantRequest(request):
    if request.method == 'POST':
        input_data = request.POST
        if not input_data:
            return JsonResponse({"error": "No input data provided"}, status=400)
        temp_merchant_data = {}

        #TODO: Find a way to get location data from merchant's input data


        #Check all the input data individually


        #Files
        if request.FILES.get('image' , None):
            temp_merchant_data['profile'] = request.FILES.get('image')
        if input_data.get('background'):
            temp_merchant_data['background'] = request.FILES.get('background')


        #Form Data Checking
        if input_data.get('name'):
            name = input_data.get('username')
            if MerchantData.objects.filter(name=name).exists():
                return JsonResponse({"error": "Username already exists"}, status=400)
            temp_merchant_data['name'] = input_data.get('name')
        if input_data.get('display_name'):
            temp_merchant_data['display_name'] = input_data.get('display_name')
        if input_data.get('address'):
            temp_merchant_data['address'] = input_data.get('address')
        if input_data.get('description'):
            temp_merchant_data['description'] = input_data.get('description')
        if input_data.get('latitude'):
            temp_merchant_data['latitude'] = input_data.get('latitude')
        if input_data.get('longitude'):
            temp_merchant_data['longitude'] = input_data.get('longitude')
        if input_data.get('hours'): #Dictionary
            temp_merchant_data['hours'] = input_data.get('hours')

        initial_products = {}
        if input_data.get('products'):
            for product in input_data.get('products'):
                initial_products.append(product)
        if not initial_products:
            return JsonResponse({"error": "No products provided"}, status=400)
        
        #Create the merchant data so we can use the pk later
        merchantObject = MerchantData.objects.create(**temp_merchant_data)
        productErrors = None

        #Create the initial products
        productCreationStatus = createInitialProducts(initial_products , merchantObject)
        productErrors = productCreationStatus['errors']
        if productCreationStatus['success'] == False:
            mainError = productCreationStatus['errorString']
            merchantObject.delete() #Delete the merchant data if product creation fails
            return JsonResponse({"error": mainError, "productErrors": productErrors}, status=400)
        
        #The merchant data has been created, and the initial products have been created, return success status to web

        # Still return the product errors if there were products that have not been successfully created due to these errors
        # so the user can see why some of their products were not created
        return JsonResponse({'status': 'success', 'productErrors': productErrors } , status=200) 
    return JsonResponse({'csrfToken': get_token(request)})

def getMerchantFromUsername(merchantUsername): # Utility
    merchant = MerchantData.objects.get(name=merchantUsername)
    return merchant

def getMerchantFromId(merchantId): # Utility
    merchant = MerchantData.objects.get(pk=merchantId)
    return merchant

def getAllProductsOfMerchant(request): # Request
    if request.method == 'POST':
        input_data = request.POST
        merchantId = input_data['merchant_id']
        if not merchantId:
            return JsonResponse({"error": "Merchant ID is required"}, status=400)
        merchant = getMerchantFromId(merchantId)
        if not merchant:
            return JsonResponse({"error": "Merchant not found"}, status=404)
        products = listAllProducts(merchant)
        return JsonResponse({"products": products}, status=200)


#Paninda --------------------------------

def listAllProducts(merchant): # Utility
    products = []
    for product in Paninda.objects.filter(merchant_pk=merchant.pk):
        products.append(product)
    return products



def createInitialProducts(initial_products , merchantObject): # Utility
    status = {
        'sucess': False,
        'errorString': "No products provided", #Default error message
        'errors': {}
    }
    totalProducts = 0
    products = []

    merchant_id = merchantObject.pk
    #Check product data
    for i, productData in initial_products:
        productStatus = createProductObject(productData , merchant_id)
        if productStatus['success'] == True:
            products.append(productStatus['product']) #Add the product to the list only if it is valid
        else:
            status['errors']["Product #" + str(i+1)] = productStatus['errorString']
    #Create the Product Objects
    for productData in products:
        totalProducts += 1
        Paninda.objects.create(**productData) #Create the products in the list

    if totalProducts > 0: #Only succeeds if there is atleast 1 product
        status['success'] = True 
    return status

def createProductObject(productData, merchantId): # Utility -- Creates a Paninda object from product data and merchant id
    status = { #Use this later to see if this function succeeds or not.
    "success": False,
    "errorString": "Unknown",
    "product": None
    }

    if not merchantId:
        status['errorString'] = "Merchant ID is required"
        return status
    if not productData:
        status['errorString'] = "No product data provided"
        return status
    
    temporary_product_data = {} # Create an empty dictionary
    

    # Check individual values if valid
    if not productData['name']:
        status['errorString'] = "No product name provided"
        return status
    if not productData['price']:
        status['errorString'] = "No product price provided"
        return status
    if not productData['availability']:
        status['errorString'] = "Invalid Availability"
        return status
    if not productData['type']:
        status['errorString'] = "Invalid Product Type"
        return status
    if not productData['image']:
        status['errorString'] = "No product image provided"
        return status
    

    # Set the values
    temporary_product_data['merchant_pk'] = merchantId # Set the product's merchant id
    temporary_product_data['name'] = productData['name']
    temporary_product_data['price'] = productData['price']
    temporary_product_data['availability'] = productData['availability']
    temporary_product_data['uri'] = productData['type']
    temporary_product_data['image'] = productData['image']

    status['product'] = temporary_product_data
    status['success'] = True
    return status