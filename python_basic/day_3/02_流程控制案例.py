'''
综合案例
答题闯关挑战赛一共3个关卡(每个关卡只有一道题)，
答对进入下一关，3关都通过则挑战成功!。答错可重试，
每道题都有3次回答机会，若3次均答错，则挑战失败，游戏自动结束。
如果用户输入为空，则提示重新作答，且不浪费回答机会。如果用户输入字母q，则直接退出游戏。
'''
answer_right = 0

for i in range(1, 4):
    is_quit = False  # 是否退出
    # answer_count = 0  # 记录回答每题的回答次数
    print(f'请回答第{i}道题')
    j = 1
    while j < 4:
        answer = input(f'{i}+5 = ?')
        if answer is None or answer == '':
            print(f'输入为空，请重新回答，还有{4 - j}次答题机会')
            continue
        elif answer == 'q' or answer == 'Q':
            is_quit = True
            break

        if int(answer) == i + 5:
            answer_right += 1
            print('回答正确！进入下一题')
            break
        else:
            # answer_count += 1
            j += 1
            if j < 4:
                print(f'回答错误，还有{4 - j}次回答机会')
            else:
                is_quit = True
                break
            continue
    # if answer_count == 3:
    #     print('答题机会已用完，游戏结束！！！')
    #     break
    # if is_quit:
    #     print('退出游戏')
    #     break
    if is_quit:
        print('游戏结束！')
        break
if answer_right == 3:
    print(f'恭喜你，答对{answer_right}道题，挑战成功！')
