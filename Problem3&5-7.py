import ParameterClasses as P
import MarkovModelClasses as MarkovCls
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs
import InputData as Data
import scr.FormatFunctions as F

#Problem 3: Markov Model (Weight 5): Develop a Markov model to simulate 2,000 patients over 50 years
# to estimate the expected life-years of a patient who is in state “Well” at the beginning of the simulation period.
# Provide 95% confidence intervals for your estimates.
# create a cohort
cohort = MarkovCls.Cohort(
    id=0,
    drug=P.Therapies.nodrug)

# simulate the cohort
simOutputs = cohort.simulate()


survival_mean_CI_text = F.format_estimate_interval(
        estimate=simOutputs.get_sumStat_survival_times().get_mean(),
        interval=simOutputs.get_sumStat_survival_times().get_t_CI(alpha=Data.ALPHA),
        deci=2)
print("Estimate of mean survival time and {:.{prec}%} confidence interval if no drug is used:".format(1 - Data.ALPHA, prec=0),
          survival_mean_CI_text)


#Problem 5: Modeling the effect of anticoagulation (Weight 2): Use your model to estimate the life-years of a patient
# who start in state “Well” and will receive this anticoagulation while in the state “Post-Stroke”.
# Provide 95% confidence intervals.

# create a cohort
cohort2 = MarkovCls.Cohort(
    id=0,
    drug=P.Therapies.anticoagulation)

# simulate the cohort
simOutputs2 = cohort2.simulate()
survival_mean_CI_text2 = F.format_estimate_interval(
        estimate=simOutputs2.get_sumStat_survival_times().get_mean(),
        interval=simOutputs2.get_sumStat_survival_times().get_t_CI(alpha=Data.ALPHA),
        deci=2)
print("  Estimate of mean survival time and {:.{prec}%} confidence interval if anticoagulation is used:".format(1 - Data.ALPHA, prec=0),
      survival_mean_CI_text2)


#Problem 6: Survival curves (Weight 2): Estimate the survival curves of
# a patient who start in state “Well” under both alternatives.

PathCls.graph_sample_path(
    sample_path=simOutputs.get_survival_curve(),
    title='Survival curve if no drug is used',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )


#a patient with anticoagulation

PathCls.graph_sample_path(
    sample_path=simOutputs2.get_survival_curve(),
    title='Survival curve if anticoagulation is used',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )


#Problem 7: Number of strokes (Weight 2): Estimate the mean and show the histogram of the number of stokes
# that an individual who start in state “Well” may experience under both alternatives.

#get mean number of strokes
stroke_mean_CI_text = F.format_estimate_interval(
        estimate=simOutputs.get_sumState_stroketimes().get_mean(),
        interval=simOutputs.get_sumState_stroketimes().get_t_CI(alpha=Data.ALPHA),
        deci=2)
print("  Estimate of mean times of stroke and {:.{prec}%} confidence interval if no drug is used:".format(1 - Data.ALPHA, prec=0),
      stroke_mean_CI_text)

# graph histogram of the number of strokes
Figs.graph_histogram(
    data=simOutputs.get_stroke_times(),
    title='Times of Stroke if the patient takes no drug',
    x_label='Survival time (years)',
    y_label='Counts',
    bin_width=1
)

#get mean number of strokes
stroke_mean_CI_text2 = F.format_estimate_interval(
        estimate=simOutputs2.get_sumState_stroketimes().get_mean(),
        interval=simOutputs2.get_sumState_stroketimes().get_t_CI(alpha=Data.ALPHA),
        deci=2)
print("  Estimate of mean times of stroke and {:.{prec}%} confidence interval if anticoagulation is used:".format(1 - Data.ALPHA, prec=0),
      stroke_mean_CI_text2)

# graph histogram of the number of strokes
Figs.graph_histogram(
    data=simOutputs2.get_stroke_times(),
    title='Times of Stroke if the patient takes anticoagulation',
    x_label='Survival time (years)',
    y_label='Counts',
    bin_width=1
)