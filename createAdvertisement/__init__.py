import azure.functions as func
import pymongo

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = "mongodb://nano-project2-cosmos-db:qlKXXAzEfR2M4wEH6uEG3ccas7leyxrXKzKLpzeRTy8W2R1D0MvJAsHnOLaR0d5JmDldGAn0o0LuC0okw600Wg==@nano-project2-cosmos-db.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@nano-project2-cosmos-db@"  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['project2-db']
            collection = database['advertisements']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )