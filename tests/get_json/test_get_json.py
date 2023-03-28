from dotenv import load_dotenv


load_dotenv()


def test_get_json():
    from getjson.lambda_function import lambda_handler

    response = lambda_handler("", "")

    assert len(response) != 0


def test_content():
    from getjson.lambda_function import lambda_handler

    response = lambda_handler("", "")
    print(response) 
    assert 1 ==1

def test_any():
    from getjson.lambda_function import lambda_handler

    response = lambda_handler("", "")
    print(response) 
    assert 0 == 0