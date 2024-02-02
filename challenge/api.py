from fastapi import FastAPI, HTTPException
from challenge import model
import pandas as pd


app = FastAPI()
model = model.DelayModel()

@app.get("/health", status_code=200)
async def get_health() -> dict:
    return {
        "status": "OK"
    }

@app.post("/predict", status_code=200)
async def post_predict(flight_data: dict) -> dict:
    try:
        # Checks if the model has been trained
        if model._model is None:
            raise HTTPException(status_code=400, detail="Model has not been trained")

        # Converts the received data to DataFrame
        data = pd.DataFrame([flight_data])

        # Preprocess the data
        features = model.preprocess(data)

        # Make predictions
        prediction = model.predict(features)

        return {"prediction": prediction}
    
    except HTTPException as http_exc:
        # Re-raise HTTPException with the same status code and details
        raise http_exc
    
    except Exception as exc:
    # Catch other exceptions and raise HTTPException with a 400 status code and details
        raise HTTPException(status_code=400, detail=str(exc))