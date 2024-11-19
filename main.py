#!/usr/bin/env python
import sys
from textwrap import dedent
from flask import Flask, jsonify, request
#from mainframe_userstory_demo.MainframeUserstoryDemoCrew import MainframeUserstoryDemoCrew
from mainframe_codegen_demo.MainframeJavaCodeDemoCrew import MainframeJavaCodeDemoCrew

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding necessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    try:
        print("Reached upto here")
        # Get the topic from the request JSON
        request_data = request.get_json()
        topic = request_data.get('topic', '')
        print(topic)
        
        if not topic:
            return jsonify({'error': 'Topic is required'}), 400

        inputs = {
            'topic': dedent(topic)
        }
        
        # Call the existing run logic
        result = MainframeJavaCodeDemoCrew().crew().kickoff(inputs=inputs)

        # Debug information about the result type
        print(f"Type of result: {type(result)}")
        print(f"Result value: {result}")

        # Custom response formatting
        response_data = {
            'status': 'success',
            #'timestamp': datetime.datetime.now().isoformat(),
            'data': str(result)
        }
        
        return jsonify(response_data), 200
    
    except Exception as e:
        error_response = {
            'status': 'error',
            #'timestamp': datetime.datetime.now().isoformat(),
            'error': str(e),
            'type': type(e).__name__
        }
        return jsonify(error_response), 500



def run():
    """
    Welcome to Java Code Generator Crew.
    """
    inputs = {
        'topic':dedent(f""" 
                User Story 1: As a Credit Card Holder, I want to check if my account balances are sufficient for credit card bill payment, so that I can avoid any overdraft fees.

                Acceptance Criteria:
                - The system retrieves the balance of the Savings Account (savings_balance) and Current Account (current_balance).
                - The primary_account is selected based on which account has a higher balance.
                - If neither account has a sufficient balance, the system checks if the primary_account balance is greater than or equal to the Minimum Bill Pay Amount.

                Technical Notes: This user story requires integration with mainframe systems to access and retrieve account balances. It also relies on the system's ability to perform conditional logic based on the account balances.

                Dependencies:
                - Mainframe account balance retrieval API
                - Conditional logic implementation
            """)
    }
    MainframeJavaCodeDemoCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        #MainframeUserstoryDemoCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
        MainframeJavaCodeDemoCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        MainframeJavaCodeDemoCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        MainframeJavaCodeDemoCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
    

# Add Flask app runner
if __name__ == '__main__':
    # Check if we want to run as API or command line
    if len(sys.argv) > 1 and sys.argv[1] == 'api':
        # Run as Flask app
        app.run(host='0.0.0.0', port=5003, debug=False)
    else:
        # Run as command line
        run()
