import scr.FormatFunctions as Format
import scr.FigureSupport as Figs
import scr.StatisticalClasses as Stat
import Parameters as P


def print_outcomes(sim_output, strategy_name):
    """ prints the outcomes of a simulated set of games under transient state
    :param multi_games: output of a simulated set of games
    :param strategy_name: the name of the heads probability
    """

    # mean and prediction interval text of game reward
    reward_mean_PI_text = Format.format_estimate_interval(
        estimate=sim_output.get_mean_total_reward(),
        interval=sim_output.get_PI_total_reward(alpha=P.alpha),
        deci=1)

    # print game reward statistics
    print(strategy_name)
    print("  Estimate of the mean game reward and {:.{prec}%} prediction interval:".format(1 - P.alpha, prec=0),
          reward_mean_PI_text)


def draw_histograms(multi_games_fair_coin, multi_games_unfair_coin):
    """ draws the histograms of average game rewards
    :param multi_games_fair_coin: multiple sets of games simulated when the coin is fair
    :param multi_games_unfair_coin: multiple sets of games simulated when the coin is unfair
    """

    # histograms of average game rewards
    set_of_game_rewards = [
        multi_games_fair_coin.get_all_total_rewards(),
        multi_games_unfair_coin.get_all_total_rewards()
    ]

    # graph histograms
    Figs.graph_histograms(
        data_sets=set_of_game_rewards,
        title="Histogram of the Gambler's Average Total Game Rewards",
        x_label='Mean Game Rewards',
        y_label='Count',
        bin_width=40,
        legend=['Fair coin', 'Unfair coin'],
        transparency=0.6,
    )


def print_comparative_outcomes(multi_games_fair_coin, multi_games_unfair_coin):
    """ prints the expected increase in average game rewards when the coin is unfair
    :param multi_games_fair_coin: multiple sets of games simulated when the coin is fair
    :param multi_games_unfair_coin: multiple sets of games simulated when the coin is unfair
    """

    # increase in game reward
    increase = Stat.DifferenceStatIndp(
        name='Increase in game reward',
        x=multi_games_unfair_coin.get_all_total_rewards(),
        y_ref=multi_games_fair_coin.get_all_total_rewards()
    )
    # estimate and prediction interval
    estimate_PI = Format.format_estimate_interval(
        estimate=increase.get_mean(),
        interval=increase.get_PI(alpha=P.alpha),
        deci=1
    )
    print("Expected increase in the average game reward and {:.{prec}%} prediction interval:".format(1 - P.alpha, prec=0),
          estimate_PI)
