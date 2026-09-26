from qrs_detector import QRS_Detector
import wfdb
import matplotlib.pyplot as plt

# ---- EXAMPLE USAGE via mit-bih arythmia dataset---- 
record=wfdb.rdrecord('MIT/100')
fs=record.fs
ecg=record.p_signal[:,0]
ann=wfdb.rdann('MIT/100','atr')
peak_samples=ann.sample 

# --- define a QRS_Detector class and feed it with a ecg numpy array and the coresponding fs
detector=QRS_Detector(ecg,fs)
r_peaks=detector.R_detect()

plt.plot(ecg)
plt.scatter(peak_samples,ecg[peak_samples],label='Labeled MIT')
plt.scatter(r_peaks,ecg[r_peaks],label='Proposal R-Detection Method')
plt.legend()
plt.show()

