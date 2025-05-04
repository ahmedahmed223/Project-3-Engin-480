from topfarm.recorders import TopFarmListRecorder
import matplotlib.pyplot as plt

recorder = TopFarmListRecorder().load(
    '/Users/a18573/VSCode/Project 3/Project-3-Engin-480/Project4/recordings/optimization_vw1.pkl'
)

plt.figure()
plt.plot(recorder['counter'], recorder['AEP']/recorder['AEP'][-1])
plt.xlabel('Iterations')
plt.ylabel('AEP/AEP_opt')
plt.show()
print('done')
