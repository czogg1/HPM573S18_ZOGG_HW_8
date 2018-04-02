import Parameters as P
import Classes as Cls
import SupportSteadyState as Support
import scr.FigureSupport as figureLibrary

# create a set of games when the coin is fair
gamesFair = Cls.SetOfGames(
    id=1,
    n_games=P.n_games,
    prob_head=P.prob_head)
# simulate the games
sim_output_fair_coin = gamesFair.simulation()

# create a set of games when the coin is unfair
gamesUnfair = Cls.SetOfGames(
    id=2,
    n_games=P.n_games,
    prob_head=P.prob_head*P.unfairness_ratio)
# simulate the games
sim_output_unfair_coin = gamesUnfair.simulation()


# print outcomes of each cohort
Support.print_outcomes(sim_output_fair_coin, 'When the coin is fair, P(head)=0.50:')
Support.print_outcomes(sim_output_unfair_coin, 'When the coin is unfair, P(head)=0.45:')

# draw survival curves and histograms
Support.draw_survival_curves_and_histograms(sim_output_fair_coin, sim_output_unfair_coin)

# print comparative outcomes
Support.print_comparative_outcomes(sim_output_fair_coin, sim_output_unfair_coin)


# check against the output from HW6:

# Trial 1 #
# Calculate expected reward of 1000 games
trial1 = Cls.SetOfGames(prob_head=0.50, n_games=1000, id=1)
test1 = trial1.simulation()

print("")
print("Checking against the output from HW6 code:")
print("  The expected game reward given P(head)=0.50:", test1.get_ave_reward())
print("  The 95%CI of the expected reward:", test1.get_CI_reward(0.05))

# Create histogram of winnings
figureLibrary.graph_histogram(
    data=trial1.get_rewards(),
    title="Histogram of Rewards from 1000 Games",
    x_label="Game Rewards",
    y_label="Frequency")

# Trial 2 #
# Calculate expected reward of 1000 games
trial2 = Cls.SetOfGames(prob_head=0.45, n_games=1000, id=2)
test2 = trial2.simulation()

print("  The expected game reward given P(head)=0.45:", test2.get_ave_reward())
print("  The 95%CI of the expected reward:", test2.get_CI_reward(0.05))

# Create histogram of winnings
figureLibrary.graph_histogram(
    data=trial2.get_rewards(),
    title="Histogram of Rewards from 1000 Games",
    x_label="Game Rewards",
    y_label="Frequency")
