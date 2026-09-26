from prominence_delineator import ProminenceDelineator 
import numpy as np 
class QRS_Detector:
    def __init__(self,clean_signal,fs):
        self.ecg=clean_signal
        self.fs=fs
    def R_detect(self):
        fs=self.fs
        sig=self.ecg
        PromDelineator = ProminenceDelineator(sampling_frequency=fs)
        # chunk it to 60 seconds segments (with overlap)
        chunks=int(len(sig)/(180*60))
        segment=int(len(sig)/chunks)
        overlap=fs # 1 Second
        overlap_start=overlap
        overlap_end=overlap
        peaks=[]
        for i in range(chunks):
            if(i==0):
                overlap_start=0
            elif(i==chunks-1):
                overlap_end=0
            else:
                overlap_start,overlap_end=overlap,overlap
            start=i*segment-overlap_start
            end=(i+1)*segment+overlap_end
            r_peaks=PromDelineator.find_rpeaks(sig[start:end])
            r_peaks=np.array(r_peaks)
            r_peaks=r_peaks.astype(int)
            mask= (r_peaks > overlap_start) & (r_peaks < segment+overlap_start)
            r_valid=r_peaks[mask]
            r_valid=r_valid+i*segment-overlap_start
            r_valid=r_valid.astype(int)     
            for j in r_valid:
                peaks.append(j)
            print(f'processed chunk{i+1}')
        peaks=np.array(peaks)
        return peaks
    
    def ECG_Delineate(self):
        pass 
