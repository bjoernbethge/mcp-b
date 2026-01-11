#!/usr/bin/env python3
"""
Performance benchmark for MCP-B optimizations.

Tests the performance of key operations to ensure optimizations
provide measurable improvements.
"""

import time
import statistics
from mcp_b import (
    MCBAgent, MCBProtocol, encode_mcb, decode_mcb,
    AMUM, quick_alignment,
    QCI, BreathingCycle,
    ETHIC, check_ethical, EthicCategory,
    start_workflow, get_engine,
)


def benchmark(func, iterations=1000):
    """Run a function multiple times and return timing stats."""
    times = []
    for _ in range(iterations):
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        times.append(end - start)
    
    return {
        "mean": statistics.mean(times) * 1000,  # Convert to ms
        "median": statistics.median(times) * 1000,
        "stdev": statistics.stdev(times) * 1000 if len(times) > 1 else 0,
        "min": min(times) * 1000,
        "max": max(times) * 1000,
    }


def test_protocol_encode_decode():
    """Test protocol encoding/decoding performance."""
    def encode():
        return encode_mcb("5510", "7C1", 0b1011101010111111, "Q", {"test": True})
    
    def decode():
        return decode_mcb("5510 7C1 1011101010111111 • {\"test\": true} • Q")
    
    print("\n" + "="*60)
    print("PROTOCOL ENCODING/DECODING BENCHMARK")
    print("="*60)
    
    encode_stats = benchmark(encode, iterations=5000)
    print(f"\nEncode (5000 iterations):")
    print(f"  Mean: {encode_stats['mean']:.4f} ms")
    print(f"  Median: {encode_stats['median']:.4f} ms")
    print(f"  Min/Max: {encode_stats['min']:.4f} / {encode_stats['max']:.4f} ms")
    
    decode_stats = benchmark(decode, iterations=5000)
    print(f"\nDecode (5000 iterations):")
    print(f"  Mean: {decode_stats['mean']:.4f} ms")
    print(f"  Median: {decode_stats['median']:.4f} ms")
    print(f"  Min/Max: {decode_stats['min']:.4f} / {decode_stats['max']:.4f} ms")


def test_amum_alignment():
    """Test AMUM alignment performance."""
    def run_alignment():
        return quick_alignment(
            intent="Test",
            divergent_3=["A", "B", "C"],
            select_1=0,
            expand_6=["1", "2", "3", "4", "5", "6"],
            select_2=0,
            converge_9=["a", "b", "c", "d", "e", "f", "g", "h", "i"],
            select_3=0
        )
    
    print("\n" + "="*60)
    print("AMUM ALIGNMENT BENCHMARK")
    print("="*60)
    
    stats = benchmark(run_alignment, iterations=1000)
    print(f"\nQuick Alignment (1000 iterations):")
    print(f"  Mean: {stats['mean']:.4f} ms")
    print(f"  Median: {stats['median']:.4f} ms")
    print(f"  Min/Max: {stats['min']:.4f} / {stats['max']:.4f} ms")


def test_qci_operations():
    """Test QCI operations performance."""
    qci = QCI()
    for i in range(100):
        qci.register_agent(f"agent{i}", initial_coherence=0.5 + (i % 50) / 100)
    
    def broadcast():
        return qci.broadcast_signal("agent0", {"test": "data"})
    
    def network_coherence():
        return qci.calculate_network_coherence()
    
    print("\n" + "="*60)
    print("QCI OPERATIONS BENCHMARK")
    print("="*60)
    
    broadcast_stats = benchmark(broadcast, iterations=1000)
    print(f"\nBroadcast Signal (1000 iterations, 100 agents):")
    print(f"  Mean: {broadcast_stats['mean']:.4f} ms")
    print(f"  Median: {broadcast_stats['median']:.4f} ms")
    print(f"  Min/Max: {broadcast_stats['min']:.4f} / {broadcast_stats['max']:.4f} ms")
    
    coherence_stats = benchmark(network_coherence, iterations=5000)
    print(f"\nNetwork Coherence (5000 iterations, 100 agents):")
    print(f"  Mean: {coherence_stats['mean']:.4f} ms")
    print(f"  Median: {coherence_stats['median']:.4f} ms")
    print(f"  Min/Max: {coherence_stats['min']:.4f} / {coherence_stats['max']:.4f} ms")


def test_ethic_checks():
    """Test ETHIC checking performance."""
    ethic = ETHIC()
    
    def check():
        return check_ethical("test_action", personal_data=False)
    
    def get_category():
        return ethic.get_by_category(EthicCategory.SAFETY)
    
    print("\n" + "="*60)
    print("ETHIC CHECKS BENCHMARK")
    print("="*60)
    
    check_stats = benchmark(check, iterations=5000)
    print(f"\nEthical Check (5000 iterations):")
    print(f"  Mean: {check_stats['mean']:.4f} ms")
    print(f"  Median: {check_stats['median']:.4f} ms")
    print(f"  Min/Max: {check_stats['min']:.4f} / {check_stats['max']:.4f} ms")
    
    category_stats = benchmark(get_category, iterations=5000)
    print(f"\nGet By Category (5000 iterations):")
    print(f"  Mean: {category_stats['mean']:.4f} ms")
    print(f"  Median: {category_stats['median']:.4f} ms")
    print(f"  Min/Max: {category_stats['min']:.4f} / {category_stats['max']:.4f} ms")


def test_workflow_operations():
    """Test workflow operations performance."""
    def create_and_run():
        wf = start_workflow("Test Task")
        step = wf.get_current_step()
        if step:
            step.options = ["A", "B", "C"]
            wf.select_and_advance(1)
        return wf
    
    print("\n" + "="*60)
    print("WORKFLOW OPERATIONS BENCHMARK")
    print("="*60)
    
    stats = benchmark(create_and_run, iterations=1000)
    print(f"\nCreate and Run Workflow (1000 iterations):")
    print(f"  Mean: {stats['mean']:.4f} ms")
    print(f"  Median: {stats['median']:.4f} ms")
    print(f"  Min/Max: {stats['min']:.4f} / {stats['max']:.4f} ms")


def main():
    """Run all benchmarks."""
    print("\n" + "#"*60)
    print("# MCP-B PERFORMANCE BENCHMARK")
    print("# Testing optimizations for speed and efficiency")
    print("#"*60)
    
    test_protocol_encode_decode()
    test_amum_alignment()
    test_qci_operations()
    test_ethic_checks()
    test_workflow_operations()
    
    print("\n" + "="*60)
    print("BENCHMARK COMPLETE")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
