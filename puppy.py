import numpy as np

print(np.random.seed(42))

#1 represents blue eyes and 0 represents hazel eyes
puppies=np.array([1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1])

p=puppies.mean()
print("Mean:",p)
print("Standard Deviation:",puppies.std())
print("Variance:",puppies.var())

#simulate 5 draws from the puppies
print(np.random.choice(puppies, size=(1,5), replace=True))
print(np.random.choice(puppies, size=(1,5), replace=True).mean())

print("Sampling distribution with size 5")
sample_props=[]
for i in range(10000):
    sample=np.random.choice(puppies, 5, replace=True)
    sample_props.append(sample.mean())
sample_props=np.array(sample_props)
print("Mean:",sample_props.mean())
print("Standard Deviation",sample_props.std())
print("Variance",sample_props.var())

print("Sampling distribution with size 20")
sample_props=[]
for i in range(10000):
    sample=np.random.choice(puppies, 20, replace=True)
    sample_props.append(sample.mean())
sample_props=np.array(sample_props)
print("Mean:",sample_props.mean())
print("Standard Deviation",sample_props.std())
print("Variance",sample_props.var())