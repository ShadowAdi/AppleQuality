# **Apple Quality Predictor**
It Is Going To Predict The Quality Of Your Apple Using Different Features Such As  `Crunchiness`,  `Softness`.
## **Goal**
The Goal Of The Project is To Give A Quality Certification About The Apple Quality.

## **Which Model**
After Using Various Model..Like `Random Forest Classifier` And `XGBoost Classifier`...And Many Other You Can See In The `AppleQuality.ipynb`
I Found **KNeigborsClassifier** As The Best Model.So I Am Going To Use It for Model Predictioons....
After Doing Grid Search CV I Find that The Model Is 0.90(90%) correct on Test Data...Which Is A Great Thing...i.e.; Out of 10 Apples Model Is Going tocorrect on 9 apples...
**Hyperparameter Tuning**:
> After Doing `HalvingGridSearchCV` i find that `n_estimators=7` are Best For Best Accuracy Score.
## **Accuracy Of Model**
I Have Used Various Classification Metrics For Model checking..Like `Accuracy Score` `F1_Score` `recall_score` and `Precision Score`
## Link To WebApp
I Have Used Streamlit For Creating A Web App And Also Deployed On Streamlit...You Can Check The Code in `App.py` File.
[Check It on Web](https://applequality-3zrskwc2ghckcmxdrlzczx.streamlit.app/)


