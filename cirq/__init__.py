# Copyright 2018 The Cirq Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from cirq._version import (
    __version__,
)

# Flattened sub-modules.

from cirq.circuits import (
    Circuit,
    CircuitDag,
    InsertStrategy,
    PointOptimizationSummary,
    PointOptimizer,
    QasmOutput,
    TextDiagramDrawer,
    Unique,
)

from cirq.devices import (
    Device,
    GridQubit,
    UnconstrainedDevice,
)

from cirq.experiments import (
    generate_supremacy_circuit_google_v2,
    generate_supremacy_circuit_google_v2_bristlecone,
    generate_supremacy_circuit_google_v2_grid,
)

from cirq.linalg import (
    allclose_up_to_global_phase,
    apply_matrix_to_slices,
    bidiagonalize_real_matrix_pair_with_symmetric_products,
    bidiagonalize_unitary_with_special_orthogonals,
    block_diag,
    commutes,
    CONTROL_TAG,
    diagonalize_real_symmetric_and_sorted_diagonal_matrices,
    diagonalize_real_symmetric_matrix,
    dot,
    expand_matrix_in_orthogonal_basis,
    hilbert_schmidt_inner_product,
    is_diagonal,
    is_hermitian,
    is_orthogonal,
    is_special_orthogonal,
    is_special_unitary,
    is_unitary,
    kak_canonicalize_vector,
    kak_decomposition,
    KakDecomposition,
    kron,
    kron_bases,
    kron_factor_4x4_to_2x2s,
    kron_with_controls,
    map_eigenvalues,
    match_global_phase,
    matrix_from_basis_coefficients,
    PAULI_BASIS,
    reflection_matrix_pow,
    slice_for_qubits_equal_to,
    so4_to_magic_su2s,
    targeted_left_multiply,
)

from cirq.line import (
    LineQubit,
)

from cirq.ops import (
    AmplitudeDampingChannel,
    ApproxPauliStringExpectation,
    AsymmetricDepolarizingChannel,
    BitFlipChannel,
    CCX,
    CCXPowGate,
    CCZ,
    CCZPowGate,
    CNOT,
    CNotPowGate,
    CSWAP,
    CSwapGate,
    CZ,
    CZPowGate,
    ControlledGate,
    DepolarizingChannel,
    EigenGate,
    FREDKIN,
    Gate,
    GateOperation,
    GeneralizedAmplitudeDampingChannel,
    H,
    HPowGate,
    I,
    IdentityGate,
    InterchangeableQubitsGate,
    ISWAP,
    ISwapPowGate,
    MeasurementGate,
    measure,
    measure_each,
    Moment,
    MultiQubitGate,
    NamedQubit,
    ControlledOperation,
    OP_TREE,
    Operation,
    ParallelGateOperation,
    Pauli,
    PauliInteractionGate,
    PauliString,
    PauliStringExpectation,
    PauliTransform,
    PhaseDampingChannel,
    PhaseFlipChannel,
    PhasedXPowGate,
    QubitId,
    QubitOrder,
    QubitOrderOrList,
    ReversibleCompositeGate,
    Rx,
    Ry,
    Rz,
    S,
    SWAP,
    SamplesDisplay,
    SingleQubitCliffordGate,
    SingleQubitGate,
    SingleQubitMatrixGate,
    SwapPowGate,
    T,
    TOFFOLI,
    ThreeQubitGate,
    TwoQubitGate,
    TwoQubitMatrixGate,
    WaveFunctionDisplay,
    X,
    XPowGate,
    XX,
    XXPowGate,
    Y,
    YPowGate,
    YY,
    YYPowGate,
    Z,
    ZPowGate,
    ZZ,
    ZZPowGate,
    amplitude_damp,
    asymmetric_depolarize,
    bit_flip,
    depolarize,
    flatten_op_tree,
    freeze_op_tree,
    generalized_amplitude_damp,
    measure,
    measure_each,
    pauli_string_expectation,
    phase_damp,
    phase_flip,
    transform_op_tree,
)

from cirq.optimizers import (
    ConvertToCzAndSingleGates,
    DropEmptyMoments,
    DropNegligible,
    EjectPhasedPaulis,
    EjectZ,
    ExpandComposite,
    is_negligible_turn,
    merge_single_qubit_gates_into_phased_x_z,
    MergeInteractions,
    MergeSingleQubitGates,
    single_qubit_matrix_to_gates,
    single_qubit_matrix_to_pauli_rotations,
    single_qubit_matrix_to_phased_x_z,
    single_qubit_op_to_framed_phase_form,
    two_qubit_matrix_to_operations,
)

from cirq.schedules import (
    Schedule,
    ScheduledOperation,
    moment_by_moment_schedule,
)

from cirq.sim import (
    bloch_vector_from_state_vector,
    density_matrix_from_state_vector,
    DensityMatrixStepResult,
    DensityMatrixSimulator,
    DensityMatrixSimulatorState,
    DensityMatrixTrialResult,
    dirac_notation,
    measure_state_vector,
    measure_density_matrix,
    sample_density_matrix,
    sample_state_vector,
    SimulatesFinalState,
    SimulatesIntermediateState,
    SimulatesIntermediateWaveFunction,
    SimulatesSamples,
    SimulationTrialResult,
    Simulator,
    SparseSimulatorStep,
    StateVectorMixin,
    StepResult,
    to_valid_density_matrix,
    to_valid_state_vector,
    validate_normalized_state,
    WaveFunctionTrialResult,
    WaveFunctionStepResult,
    WaveFunctionSimulatorState,
)

from cirq.study import (
    ComputeDisplaysResult,
    Linspace,
    ParamResolver,
    plot_state_histogram,
    Points,
    Sweep,
    Sweepable,
    to_resolvers,
    TrialResult,
    UnitSweep,
)

from cirq.value import (
    canonicalize_half_turns,
    chosen_angle_to_canonical_half_turns,
    chosen_angle_to_half_turns,
    Duration,
    PeriodicValue,
    Timestamp,
    validate_probability,
    value_equality,
)

# pylint: disable=redefined-builtin
from cirq.protocols import (
    apply_unitary,
    ApplyUnitaryArgs,
    approx_eq,
    channel,
    CircuitDiagramInfo,
    CircuitDiagramInfoArgs,
    circuit_diagram_info,
    decompose,
    decompose_once,
    decompose_once_with_qubits,
    has_channel,
    has_mixture,
    has_mixture_channel,
    has_unitary,
    inverse,
    is_parameterized,
    measurement_key,
    mixture,
    mixture_channel,
    mul,
    pauli_expansion,
    pow,
    qasm,
    QasmArgs,
    SupportsApplyUnitary,
    SupportsApproximateEquality,
    SupportsChannel,
    SupportsCircuitDiagramInfo,
    SupportsDecompose,
    SupportsDecomposeWithQubits,
    SupportsParameterization,
    SupportsPhase,
    SupportsMixture,
    SupportsQasm,
    SupportsQasmWithArgs,
    SupportsQasmWithArgsAndQubits,
    SupportsTraceDistanceBound,
    SupportsUnitary,
    resolve_parameters,
    unitary,
    validate_mixture,
    trace_distance_bound,
    phase_by,
)

from cirq.ion import (
    MS,
    two_qubit_matrix_to_ion_operations,
)
# pylint: enable=redefined-builtin

# Unflattened sub-modules.

from cirq import (
    contrib,
    google,
    testing,
)
