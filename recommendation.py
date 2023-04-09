import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
import pickle

class KNNClassifier:
    def __init__(self, n_neighbors):
        self.n_neighbors = n_neighbors
        self.model = KNeighborsClassifier(n_neighbors=self.n_neighbors)

    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)

    def score(self, X_test, y_test):
        return self.model.score(X_test, y_test)

    def confusion_matrix(self, X_test, y_test):
        y_pred = self.model.predict(X_test)
        return confusion_matrix(y_test, y_pred)

    def save_model(self, filepath):
        with open(filepath, 'wb') as file:
            pickle.dump(self.model, file)

    @staticmethod
    def load_model(filepath):
        with open(filepath, 'rb') as file:
            return pickle.load(file)


def run(age,driving_license,previously_insured,vehicle_damage,vehicle_age,vintage,region_code,policy_sale):
    mapping = {'Yes': 1, 'No': 0}
    driving_license = mapping[driving_license]
    previously_insured = mapping[previously_insured]
    vehicle_damage = mapping[vehicle_damage]
    policy_sale = float(policy_sale)
    region_code = float(region_code)
    age, vehicle_age, vintage = [float(var) for var in [age, vehicle_age, vintage]]
    class1, class2, class3 = [int(vehicle_age == i) for i in range(3)]
    v1, v2, v3, v4, v5 = [int(vintage == i) for i in range(5)]

    df = [age, driving_license, previously_insured, vehicle_damage, policy_sale, region_code, v1, v2, v3, v4, v5, class1, class2, class3]

    loaded_model = KNNClassifier.load_model('knn_model.pkl')
    pred = loaded_model.predict([df])
    return pred[0]

#print(run('51','Yes','No','Yes','0','4','28','26'))
