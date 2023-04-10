if __name__=="__main__":
    try:
        a=10/0
    except Exception as e:
        logging.info("zero error")
        raise CustomException(e,sys)