from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Veri kümesini yükle
iris = load_iris()
X = iris.data
y = iris.target

# Veriyi eğitim ve test setlerine ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Sınıflandırıcı modelini oluştur
model = GaussianNB()

# Modeli eğit
model.fit(X_train, y_train)

# Modelin performansını değerlendir
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Modelin doğruluk skoru:", accuracy)