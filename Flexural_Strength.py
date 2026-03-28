# Name: Wade:@
# Data: 2026/2/28 8:56


def process_intensity_observations_debug(observations):
    if not observations:
        print("没有提供观测值")
        return None

    data = list(observations)
    original_count = len(data)
    discard_limit = int(original_count * 0.4)
    discarded = 0
    step = 1

    print(f"初始观测值: {data}")
    print(f"舍弃 (40%): {discard_limit}\n")

    while len(data) > 0:
        print(f"---- 第 {step} 步 ----")
        print(f"目前所剩数据 : {data}")

        avg = sum(data) / len(data)
        max_val = max(data)
        min_val = min(data)

        if avg == 0:
            print("平均值为零 → 无法计算相对误差")
            return None

        max_rel_error = abs(max_val - avg) / abs(avg)
        min_rel_error = abs(min_val - avg) / abs(avg)

        print(f"平均值 = {avg:.6f},"
              f"\n最大值 = {max_val}, 相对误差 = {max_rel_error:.2%}"
              f"\n最小值 = {min_val}, 相对误差 = {min_rel_error:.2%}")

        # 确定丢弃值
        if max_rel_error >= min_rel_error:
            worst_value = max_val
            max_relative_error = max_rel_error
            source = "MAX"
        else:
            worst_value = min_val
            max_relative_error = min_rel_error
            source = "MIN"

        print(f"丢弃值 {source}: {worst_value}"
              f"\n最大相对误差 = {max_relative_error:.2%}")

        # 检查接受条件
        if max_relative_error <= 0.15:
            print("\n条件满足 (≤15%).")
            print(f"最后平均值 = {avg:.6f}")
            return avg

        # 去除丢弃值
        print(f"丢弃的观测值为: {worst_value}")
        data.remove(worst_value)
        discarded += 1

        print(f"丢弃的数目 = {discarded}")

        # 检查丢弃值的上限
        if discarded > discard_limit:
            print("\n已达到丢弃上限 (≥40%)， 需要重新实验。")
            return None

        print()
        step += 1

    print("未获取到有效结果。")
    return None

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("=" * 10 + "\t程序启动\t" + "=" * 10)

    while True:
        try:
            input_str = input("\n请输入观测值 (空格间隔每个数据，q to quit): ")
            if input_str.lower() == "q":
                break
            observations = map(float, input_str.split())
            result = process_intensity_observations_debug(observations)

            if result is not None:
                print("返回结果:", result)
            else:
                print("未获取到有效结果。")

        except Exception as e:
            print(e)
        except ValueError:
            print("请输入数字！")
