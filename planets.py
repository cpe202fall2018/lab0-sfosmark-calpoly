def weight_on_planets():
   weight = int(input("What do you weigh on Earth?"))
   marsWeight = weight * 0.38
   jupiterWieght = weight * 2.34
   print("\nOn Mars you would weigh {} pounds.\nOn Jupiter you would weigh {} pounds.".format(marsWeight, jupiterWeight))

   
if __name__ == '__main__':
   weight_on_planets()
