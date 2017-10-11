import outlier
import random
import time


def setup(wsize):
    out = outlier.Outlier(wsize, 3)
    for _ in range(wsize):
        out.add(random.randint(0, 100))
    return out


def runner(out, num_obervations):
    num_normal = 0
    num_outlier = 0

    for i in range(num_obervations):
        obs = random.randint(0, 100)
        if random.random() < 0.05:
            obs += out.std * 4 + out.mean
        if out.add_and_check(obs):
            num_outlier += 1
        else:
            num_normal += 1

    return num_normal, num_outlier


def main(wsize=10000, num_obs=1000000):
    print('Running {} observations over a window of size {}'.format(
        num_obs, wsize))

    out = setup(wsize)
    start_time = time.time()
    num_normal, num_outlier = runner(out, num_obs)
    end_time = time.time()
    run_time = end_time - start_time

    print('Window Size: {}'.format(wsize))
    print('Num observations: {}'.format(num_obs))
    print('Total Run Time: {:.2f} sec'.format(run_time))
    print('Per Obs Time {:.2f} usec'.format((run_time * 1000000) / num_obs))
    print('Num Normal Obs: {}'.format(num_normal))
    print('Num Outlier Obs: {}'.format(num_outlier))


if __name__ == '__main__':
    main()
