# Name: Wade:@
# Data: 2026/2/28 8:56
from os import name

def process_intensity_observations_debug(observations):
    """
    Debug version: prints each processing step.
    """

    if not observations:
        print("No observations provided.")
        return None

    data = list(observations)
    original_count = len(data)
    discard_limit = int(original_count * 0.4)
    discarded = 0
    step = 1

    print(f"Original observations: {data}")
    print(f"Discard limit (40%): {discard_limit}\n")

    while len(data) > 0:
        print(f"---- Step {step} ----")
        print(f"Current data: {data}")

        avg = sum(data) / len(data)
        max_val = max(data)
        min_val = min(data)

        if avg == 0:
            print("Average is zero → cannot compute relative error.")
            return None

        max_rel_error = abs(max_val - avg) / abs(avg)
        min_rel_error = abs(min_val - avg) / abs(avg)

        print(f"Average = {avg:.6f}")
        print(f"Max value = {max_val}, Relative error = {max_rel_error:.2%}")
        print(f"Min value = {min_val}, Relative error = {min_rel_error:.2%}")

        # Determine worst observation
        if max_rel_error >= min_rel_error:
            worst_value = max_val
            max_relative_error = max_rel_error
            source = "MAX"
        else:
            worst_value = min_val
            max_relative_error = min_rel_error
            source = "MIN"

        print(f"Worst observation from {source}: {worst_value}")
        print(f"Maximum relative error = {max_relative_error:.2%}")

        # Check acceptance condition
        if max_relative_error <= 0.15:
            print("\nCondition satisfied (≤15%).")
            print(f"Final average = {avg:.6f}")
            return avg

        # Remove worst value
        print(f"Removing observation: {worst_value}")
        data.remove(worst_value)
        discarded += 1

        print(f"Discarded count = {discarded}")

        # Check discard limit
        if discarded > discard_limit:
            print("\nDiscard limit reached (≥40%). Resampling required.")
            return None

        print()
        step += 1

    print("No valid result obtained.")
    return None

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("=" * 10 + "\tUser interaction examples\t" + "=" * 10)

    while True:
        try:
            input_str = input("\nPlease enter observations: ")
            if input_str.lower() == "q":
                break
            observations = map(float, input_str.split())
            result = process_intensity_observations_debug(observations)

            if result is not None:
                print("\nReturned result:", result)
            else:
                print("No valid result obtained.")

        except Exception as e:
            print(e)
        except ValueError:
            print("Please enter a number.")

    # observations = [10.2, 9.8, 10.1, 15.0, 9.9]
    # result = process_intensity_observations_debug(observations)

    # print("\nReturned result:", result)
