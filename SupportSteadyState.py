import scr.FormatFunctions as Format
# import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs
import scr.StatisticalClasses as Stat
import Parameters as P


def print_outcomes(sim_output, strategy_name):
    """ prints the outcomes of a simulated set of games under steady state
    :param sim_output: output of a simulated set of games
    :param strategy_name: the name of the heads probability
    """

    # mean and confidence interval text of game reward
    reward_mean_CI_text = Format.format_estimate_interval(
        estimate=sim_output.get_ave_reward(),
        interval=sim_output.get_CI_reward(alpha=P.alpha),
        deci=1)

    # print game reward statistics
    print(strategy_name)
    print("  Estimate of the mean game reward and {:.{prec}%} confidence interval:".format(1 - P.alpha, prec=0),
          reward_mean_CI_text)


def draw_survival_curves_and_histograms(sim_output_fair_coin, sim_output_unfair_coin):
    """ draws the histograms of game rewards
    :param sim_output_fair_coin: output of a set of games simulated when the coin is fair
    :param sim_output_unfair_coin: output of a set of games simulated when the coin is unfair
    """

    # histograms of game rewards
    set_of_game_rewards = [
        sim_output_fair_coin.get_rewards(),
        sim_output_unfair_coin.get_rewards()
    ]

    # graph histograms
    Figs.graph_histograms(
        data_sets=set_of_game_rewards,
        title='Histogram of Game Rewards',
        x_label='Game rewards',
        y_label='Counts',
        bin_width=20,
        legend=['Fair coin', 'Unfair coin'],
        transparency=0.6
    )


def print_comparative_outcomes(sim_output_fair_coin, sim_output_unfair_coin):
    """ prints the expected increase in game rewards when the coin is unfair
    :param sim_output_fair_coin: output of a set of games simulated when the coin if fair
    :param sim_output_unfair_coin: output of a set of games simulated when the coin is unfair
    """

    # increase in game reward
    increase = Stat.DifferenceStatIndp(
        name='Increase in game reward',
        x=sim_output_unfair_coin.get_rewards(),
        y_ref=sim_output_fair_coin.get_rewards()
    )
    # estimate and CI
    estimate_CI = Format.format_estimate_interval(
        estimate=increase.get_mean(),
        interval=increase.get_t_CI(alpha=P.alpha),
        deci=1
    )
    print("The average increase in game reward and {:.{prec}%} confidence interval:".format(1 - P.alpha, prec=0),
          estimate_CI)
