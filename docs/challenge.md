# Latam Challenge

In this challenge, we were able to finish the first 2 parts, where the first one (model.py) pass 4/4 tests, and the second part (api.py) completed 3/4 test.

## Fixes and bugs

1. In the `exploration.ipynb`, the `sns.barplot` function didn´t have `x` and `y` name at the arguments.
2. We improved `get_period_day(date)` method, changing the conditions to return either `mañana`, `tarde` or `noche`
3. We change how `anyio` library call `start_blocking_portal` method ([reference](https://stackoverflow.com/questions/77596485/anyio-has-no-attribute-start-blocking-portal)), if you want to run this test locally, after the installation you must change this.
4. There was a wrong use of parenthesis at Union method on `model.py`, `()` instead of `[]`
5. We change the path inside test_model.py from `"../data/data.csv"` to `"data/data.csv"`

## Model

I chose XGBoost over Logistic Regression because XGBoost offers enhanced capabilities in capturing complex relationships and non-linear patterns. Despite similar classification metrics, XGBoost provides valuable insights into feature importance, improving interpretability. It excels in handling large feature sets, exhibits robustness against overfitting, and delivers more accurate representations of underlying data patterns. The decision aligns with the goal of a comprehensive and effective solution, prioritizing predictive power and flexibility.

## Trainee Feedback

From the knowledge gained as a trainee at Latam, the challenge provides a valuable opportunity to apply various topics essential for an MLE. While I didn't complete the entire challenge, opting to prioritize building a model that passes the required tests over deploying the API on GCP, it aligns with Latam's philosophy that emphasizes completing prerequisite tasks before advancing. Nevertheless, the insights gained during the Trainee program were well-suited for the expectations of this challenge.

The area where I perceived the most knowledge gap was in model selection and optimization. As a Trainee, I believe there is a considerable distance in fully understanding the nuances and benefits of the models to be employed.