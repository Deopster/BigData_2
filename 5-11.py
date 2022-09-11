from sklearn.datasets import fetch_california_housing #5 задание
import pandas
def function(x):
    print(x.name, x.mean())

def main():
    data = fetch_california_housing(as_frame=True).get('data')
    target = fetch_california_housing(as_frame=True).get('target')
    target_names = fetch_california_housing(as_frame=True).get('target_names')
    data = pandas.concat([data, target], axis=1, names=[target_names])
    print(data)#6 задание
    data.info()#7 задание
    print(data.isna().sum())#8 задание
    print(data.loc[(data.HouseAge > 50) & (data.Population > 2500)]) #9 задание
    print("max= ", max(data.HouseAge),"min= ", min(data.HouseAge)) #10 задание
    data.apply(function, axis=0)

if __name__ == '__main__':
    main()