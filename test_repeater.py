from repeater import repeater

def test_repeater_returns_none():
    # arrange
    def dummy_function(arg):
        pass

    num_calls = 398673
    dummy_arg = {}

    # act
    result = repeater(dummy_function, num_calls, dummy_arg)

    # assert
    assert result == None

def test_repeater_invokes_function_once():

    was_called = False
    # arrange
    def dummy_function(arg):
        nonlocal was_called
        was_called = True

    # act
    repeater(dummy_function, 1, "this test does NOT care about this argument")

    assert was_called, "Expected dummy_function to be called at least once"


def test_repeater_invokes_function_multiple_times():

    times_actually_called = 0
    desired_count = 78
    # arrange
    def dummy_function(arg):
        nonlocal times_actually_called
        times_actually_called += 1

    # act
    repeater(dummy_function, desired_count, "this test does NOT care about this argument")

    assert times_actually_called == desired_count, "Expected dummy_function to be called four times"

def test_repeater_invokes_function_with_passed_argument():
    # arrange
    call_count = 6
    dummy_arg = "whatever we like"
    received_args = []
    # arrange
    def dummy_function(arg):
        nonlocal received_args
        received_args.append(arg)
    
    repeater(dummy_function, call_count, dummy_arg)

    assert received_args == [dummy_arg] * call_count

