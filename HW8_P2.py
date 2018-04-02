import Parameters as P
import Classes as Cls
import SupportTransientState as Support
import scr.FigureSupport as figureLibrary

# create multiple cohorts for when the coin is fair
multi_games_fair_coin = Cls.MultipleGameSets(
    ids=range(P.number_of_simulated_games),
    prob_head=P.prob_head,
    n_games_in_a_set=P.n_games_in_a_set)

# simulate all cohorts
multi_games_fair_coin.simulation()

# create multiple cohorts for when the coin is unfair
multi_games_unfair_coin = Cls.MultipleGameSets(
    ids=range(P.number_of_simulated_games, 2*P.number_of_simulated_games),
    prob_head=P.prob_head*P.unfairness_ratio,
    n_games_in_a_set=P.n_games_in_a_set)

# simulate all cohorts
multi_games_unfair_coin.simulation()


# print outcomes of each set of games
Support.print_outcomes(multi_games_fair_coin, 'When the coin is fair, P(head)=0.50:')
Support.print_outcomes(multi_games_unfair_coin, 'When the coin is unfair, P(head)=0.45:')

# draw histograms of average game rewards
Support.draw_histograms(multi_games_fair_coin, multi_games_unfair_coin)

# print comparative outcomes
Support.print_comparative_outcomes(multi_games_fair_coin, multi_games_unfair_coin)


# check against the output from HW6:

# Trial 1 #
# create a multiple game sets
multipleGameSets=Cls.MultipleGameSets(ids=range(1000), prob_head=0.50, n_games_in_a_set=10)
# simulate all game sets
multipleGameSets.simulation()

print("")
print("Checking against the output from HW6 code:")
# print projected mean reward
print('   Projected mean game reward',
      multipleGameSets.get_mean_total_reward())
# print projection interval
print('   95% projection interval of the average game rewards',
      multipleGameSets.get_PI_total_reward(0.05))

# plot
figureLibrary.graph_histogram(
    data=multipleGameSets.get_all_total_rewards(),
    title="Histogram of the Gambler's Total Game Rewards from 10 Games",
    x_label='Mean Game Rewards',
    y_label='Count')

# Trial 2 #
# create a multiple game sets
multipleGameSets=Cls.MultipleGameSets(ids=range(1000, 2000), prob_head=0.45, n_games_in_a_set=10)
# simulate all game sets
multipleGameSets.simulation()

# print projected mean reward
print('   Projected mean game reward',
      multipleGameSets.get_mean_total_reward())
# print projection interval
print('   95% projection interval of the average game rewards',
      multipleGameSets.get_PI_total_reward(0.05))

# plot
figureLibrary.graph_histogram(
    data=multipleGameSets.get_all_total_rewards(),
    title="Histogram of the Gambler's Total Game Rewards from 10 Games",
    x_label='Mean Game Rewards',
    y_label='Count')
