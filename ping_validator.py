#!/usr/bin/env python3

import subprocess
import time
import logging
from datetime import datetime

# set logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('validator_ping.log'),
        logging.StreamHandler()
    ]
)

# setting
STAKING_POOL_ID = "yourId.poolv1.near"  # 예: "validator.poolv1.near"
ACCOUNT_ID = "owner account id"           # 예: "validator.near"
GAS = "300000000000000"
CHECK_INTERVAL = 43200  # 1 epoch time

def send_ping():
    try:
        command = f"near call {STAKING_POOL_ID} ping '{{}}' --accountId {ACCOUNT_ID} --gas={GAS}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            logging.info("Ping 성공!")
            logging.debug(f"Output: {result.stdout}")
        else:
            logging.error(f"Ping 실패: {result.stderr}")
            
    except Exception as e:
        logging.error(f"오류 발생: {str(e)}")

def main():
    logging.info("Validator ping 스크립트 시작")
    
    while True:
        try:
            send_ping()
            logging.info(f"다음 체크까지 {CHECK_INTERVAL}초 대기")
            time.sleep(CHECK_INTERVAL)
            
        except KeyboardInterrupt:
            logging.info("스크립트 종료")
            break
        except Exception as e:
            logging.error(f"예상치 못한 오류: {str(e)}")
            time.sleep(60)  # 오류 발생시 1분 대기 후 재시도

if __name__ == "__main__":
    main()
