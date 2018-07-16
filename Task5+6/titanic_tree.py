import numpy as np 
import pandas as pd 
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from datetime import datetime
start = datetime.utcnow()
# Import data
test = pd.read_csv('test.csv')
train = pd.read_csv('train.csv')
gender = pd.read_csv('gender_submission.csv')

# XU LI DU LIEU
# -Cac bien bi thieu phai duoc dien day du
# -Cac bien dung phan loai phai de dang so

# Convent gioi tinh sang dang so, male la 0, female = 1
train.loc[train["Sex"] == "male", "Sex"] = 0
train.loc[train["Sex"] == "female", "Sex"] = 1

# DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None, **kwargs)
# Fill NA/NaN values using the specified method
# Thay the cac gia gi NaN trong "Embarked" = "S"
train["Embarked"] = train['Embarked'].fillna("S")

# DataFrame.median(axis=None, skipna=None, level=None, numeric_only=None, **kwargs)
# Return the median of the values for the requested axis
# Thay the cac gia tri NaN trong "Age" = gia tri trung binh cua "Age"
train['Age'] = train['Age'].fillna(train['Age'].median())

# Convent Embarked thanh dang so
train.loc[train["Embarked"] == "S", "Embarked"] = 0
train.loc[train["Embarked"] == "C", "Embarked"] = 1
train.loc[train["Embarked"] == "Q", "Embarked"] = 2

# XU LI CAC GIA TRI NaN VOI test data
test.loc[test["Sex"] == "male", "Sex"] = 0
test.loc[test["Sex"] == "female", "Sex"] = 1
test['Fare'] = test['Fare'].fillna(test['Fare'].median())
test['Age'] = test['Age'].fillna(test['Age'].median())
test.loc[test["Embarked"] == "S", "Embarked"] = 0
test.loc[test["Embarked"] == "C", "Embarked"] = 1
test.loc[test["Embarked"] == "Q", "Embarked"] = 2

# CHON target VA CAC feature

target = train["Survived"].values
features = train[["Pclass","Age","Sex","Fare", "SibSp", "Parch", "Embarked"]].values
# Do sau toi da cua cay
max_depth = 10
# So luong mau toi thieu de tach mot node
min_samples_split = 5

#  HUAN LUYEN CO XU LY overfit
my_tree = tree.DecisionTreeClassifier(max_depth = max_depth, min_samples_split = min_samples_split, random_state = 2)
my_tree = my_tree.fit(features, target)
print( my_tree.score(features, target))

# LUU CAC DAC DIEM DUNG DE TEST
test_features = test[["Pclass", "Age", "Sex", "Fare", "SibSp", "Parch", "Embarked"]].values

# THUC HIEN DU DOAN
tree_prediction = my_tree.predict(test_features)

# XU LI KET QUA
PassengerId =np.array(test["PassengerId"]).astype(int)
tree_solution = pd.DataFrame(tree_prediction, PassengerId, columns = ["Survived"])

# print(tree_solution[["Survived"]].values)
end = datetime.utcnow()
print("Thoi gian thuc hien ca 2 thuat toan")
print(end - start)
# LUU TRU KET QUA
tree_solution.to_csv("tree_solution.csv", index_label = ["PassengerId"])



