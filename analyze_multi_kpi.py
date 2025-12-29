import pandas as pd
import os
import json
import logging

with open("config.json","r") as f:
    config= json.load(f)    
input_folder = config["input_folder"]
traffic_column = config["traffic_column"]  
throughput_column = config["throughput_column"]
latency_column = config["latency_column"]
log_file = config["log_file"]
output_file = config["output_file"]

logging.basicConfig(
    filename=log_file,
    level= logging.INFO,
    format= "%(asctime)s - %(levelname)s - %(message)s"
)

logging.info(f"Script Started")
#-----------------define analyze KPI function-----------------------------

def analyze_kpi(filepath, column_name):
    try:
        df = pd.read_excel(filepath)

        if column_name not in df.columns:
            raise KeyError(f"{column_name} not found")

        if column_name == traffic_column:
            df[column_name] = pd.to_numeric(df[column_name], errors="coerce")
            count = df[column_name].notna().sum ()
            if count !=0:
                total = df[column_name].sum()


                if total == 0:
                    flag = "YES"
                else:
                    flag = "NO"
            else:
                flag = "MISSING"
                total ="MISSING"

            return total, flag

        elif column_name == throughput_column:
            df[column_name] = pd.to_numeric(df[column_name], errors="coerce")
            count = df[column_name].notna().sum ()
            if count !=0:
                throughput = df[column_name].mean()
                if throughput <5:
                    throughput_flag = "LOW"
                else:
                    throughput_flag = "OK"
            else:
                throughput_flag = "MISSING"
                throughput ="MISSING"
            
                
            return throughput, throughput_flag

        elif column_name == latency_column:
            
            df[column_name] = pd.to_numeric(df[column_name], errors="coerce")
            count = df[column_name].notna().sum ()
            if count !=0:
                latency = df[column_name].mean()
                if latency >100:
                    latency_flag = "HIGH"

                else: latency_flag = "OK"
                
                    
                    
            else:
                latency ="MISSING"
                latency_flag = "MISSING"

                    
            return latency, latency_flag

    except KeyError as c:
        logging.error(f"{column_name} column not found in {filepath}")
        return None, None
    except Exception as e:
        logging.error(f"Error in file {filepath}: {e}")
        return None, None
    

#-----------------------------end of function---------------------------------------------------
Result = []
for file in os.listdir(input_folder):
    
    if file.endswith(".xlsx"):
        logging.info(f"{file} file processing....")

        file_path = os.path.join(input_folder, file)

        total_traffic, zero_flag = analyze_kpi(file_path, traffic_column)
        throughput_val, throughput_flag = analyze_kpi(file_path, throughput_column)
        latency_val, latency_flag = analyze_kpi(file_path, latency_column)

        Result.append([file, total_traffic, zero_flag, throughput_val, throughput_flag, latency_val, latency_flag ])
        logging.info(f"{file} file processed succesfully...")


summary_df = pd.DataFrame(Result, columns=["File", "Traffic", "Traffic_Flag", "DL_Throughput", "DL_Throughput_Flag", "Latency", "Latency_Flag"])

summary_df.to_excel(output_file, index=False)
logging.info("Script Finished")
  

    
